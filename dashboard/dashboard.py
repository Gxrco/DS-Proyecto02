import json
import pickle
import warnings
from pathlib import Path

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from sentence_transformers import SentenceTransformer

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Dashboard", layout="wide")

# Configuración de rutas
DASHBOARD_DIR = Path(__file__).parent
PROJECT_ROOT = DASHBOARD_DIR.parent
MODELS_DIR = PROJECT_ROOT / "sBertModel"
INDIVIDUAL_MODELS_DIR = MODELS_DIR / "individual_models"
MODEL_OUTPUTS_DIR = MODELS_DIR / "model_outputs"

# Función para cargar modelos
@st.cache_resource
def load_sbert_model():
    """Carga el modelo sBERT para generar embeddings"""
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def load_model(model_path):
    """Carga un modelo pickle"""
    with open(model_path, "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_encoders():
    """Carga los label encoders"""
    encoder_category = load_model(MODEL_OUTPUTS_DIR / "label_encoder_category.pkl")
    encoder_misconception = load_model(MODEL_OUTPUTS_DIR / "label_encoder_misconception.pkl")
    return encoder_category, encoder_misconception


@st.cache_data(show_spinner=False)
def load_algorithm_metrics():
    """Carga métricas pre-calculadas para cada algoritmo"""
    metrics_path = MODEL_OUTPUTS_DIR / "algorithm_metrics.json"
    if not metrics_path.exists():
        return None, None

    with open(metrics_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    metrics = payload.get("metrics", {})
    if not metrics:
        return payload, pd.DataFrame()

    metrics_df = (
        pd.DataFrame.from_dict(metrics, orient="index")
        .reset_index()
        .rename(columns={"index": "algorithm"})
    )
    return payload, metrics_df

# Función para crear el texto de entrada
def create_input_text(question, answer, explanation):
    """Combina Question + Answer + Explanation para sBERT"""
    parts = []
    if question and question.strip():
        parts.append(str(question))
    if answer and answer.strip():
        parts.append(f"Answer: {answer}")
    if explanation and explanation.strip():
        parts.append(f"Explanation: {explanation}")
    return " ".join(parts)

# Función de predicción jerárquica
def hierarchical_predict_top_k(features, category_model, misconception_model,
                                 category_encoder, misconception_encoder, top_k=3):
    """
    Pipeline jerárquico para generar predicciones Category:Misconception.
    """
    n_samples = features.shape[0]
    predictions = []

    # Predecir Category con probabilidades
    category_probs = category_model.predict_proba(features)

    for i in range(n_samples):
        sample_predictions = []

        # Obtener top categorías ordenadas por probabilidad
        top_category_indices = np.argsort(category_probs[i])[::-1]

        for cat_idx in top_category_indices:
            category = category_encoder.inverse_transform([cat_idx])[0]
            cat_prob = category_probs[i][cat_idx]

            # Verificar si esta categoría requiere Misconception
            if 'Misconception' in category:
                if misconception_model is not None:
                    # Obtener probabilidades de misconceptions
                    misc_probs = misconception_model.predict_proba(features[i:i+1])[0]

                    # Top 3 misconceptions
                    top_misc_indices = np.argsort(misc_probs)[::-1][:3]

                    for misc_idx in top_misc_indices:
                        misconception = misconception_encoder.inverse_transform([misc_idx])[0]
                        combined_prob = cat_prob * misc_probs[misc_idx]

                        sample_predictions.append({
                            'label': f"{category}:{misconception}",
                            'prob': combined_prob
                        })
                else:
                    sample_predictions.append({
                        'label': f"{category}:NA",
                        'prob': cat_prob
                    })
            else:
                sample_predictions.append({
                    'label': f"{category}:NA",
                    'prob': cat_prob
                })

        # Ordenar por probabilidad y tomar top-k
        sample_predictions = sorted(sample_predictions, key=lambda x: x['prob'], reverse=True)

        predictions.append(sample_predictions[:top_k])

    return predictions

st.title("Dashboard de Análisis de Explicaciones Estudiantiles")

tab1, tab2, tab3 = st.tabs(
    ["Dashboard Interactivo", "Resultados por Algoritmo", "Clasificación de Explicaciones"]
)

with tab3:
    st.markdown("## Clasificación de Nuevas Explicaciones Estudiantiles")
    st.markdown("Ingrese los datos de una explicación estudiantil para clasificarla usando los modelos entrenados.")

    # Formulario de entrada
    with st.form("classification_form"):
        st.markdown("### Datos de Entrada")

        col1, col2 = st.columns(2)

        with col1:
            row_id = st.text_input("Row ID (opcional)", placeholder="36696")
            question_id = st.text_input("Question ID (opcional)", placeholder="31772")

        with col2:
            mc_answer = st.text_input("MC Answer", placeholder="\\( \\frac{1}{3} \\)")

        question_text = st.text_area(
            "Question Text",
            placeholder="What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]",
            height=100
        )

        student_explanation = st.text_area(
            "Student Explanation",
            placeholder="I think that 1/3 is the answer, as it's the simplest form of 3/9.",
            height=100
        )

        # Selector de modelo
        st.markdown("### Selección de Modelo")
        model_choice = st.selectbox(
            "Seleccione el modelo de clasificación:",
            ["Random Forest", "SVM", "MLP"],
            index=0
        )

        submit_button = st.form_submit_button("Clasificar")

    # Procesamiento cuando se envía el formulario
    if submit_button:
        if not question_text or not mc_answer or not student_explanation:
            st.error("Por favor, complete al menos los campos: Question Text, MC Answer y Student Explanation")
        else:
            with st.spinner("Cargando modelos y generando predicción..."):
                try:
                    # Cargar modelos necesarios
                    sbert_model = load_sbert_model()
                    encoder_category, encoder_misconception = load_encoders()
                    misconception_model = load_model(MODEL_OUTPUTS_DIR / "misconception_model.pkl")

                    # Seleccionar modelo de categoría según elección del usuario
                    if model_choice == "Random Forest":
                        category_model = load_model(INDIVIDUAL_MODELS_DIR / "category_model_rf.pkl")
                    elif model_choice == "SVM":
                        category_model = load_model(INDIVIDUAL_MODELS_DIR / "category_model_svm.pkl")
                    else:  # MLP - Modelo mejorado con SMOTE + Class Weights
                        category_model = load_model(MODEL_OUTPUTS_DIR / "improved_classifier_smote_cw.pkl")

                    # Crear texto de entrada
                    input_text = create_input_text(question_text, mc_answer, student_explanation)

                    # Generar embedding
                    embedding = sbert_model.encode([input_text], convert_to_numpy=True)

                    # Realizar predicción
                    predictions = hierarchical_predict_top_k(
                        embedding,
                        category_model,
                        misconception_model,
                        encoder_category,
                        encoder_misconception,
                        top_k=3
                    )

                    # Mostrar resultados
                    st.success("Clasificación completada!")

                    st.markdown(f"### Resultados con modelo: **{model_choice}**")

                    # Mostrar datos de entrada
                    with st.expander("Ver datos de entrada"):
                        input_data = {
                            "Row ID": row_id if row_id else "N/A",
                            "Question ID": question_id if question_id else "N/A",
                            "Question Text": question_text,
                            "MC Answer": mc_answer,
                            "Student Explanation": student_explanation
                        }
                        st.json(input_data)

                    # Mostrar predicciones Top-3
                    st.markdown("#### Top 3 Predicciones")

                    for idx, pred in enumerate(predictions[0], 1):
                        label = pred['label']
                        prob = pred['prob']

                        # Separar categoría y misconception
                        parts = label.split(':')
                        category = parts[0]
                        misconception = parts[1] if len(parts) > 1 else "N/A"

                        # Crear columnas para mostrar la predicción
                        col1, col2, col3 = st.columns([1, 2, 1])

                        with col1:
                            st.metric(f"#{idx}", f"{prob*100:.2f}%")

                        with col2:
                            st.markdown(f"**Categoría:** {category}")
                            if misconception != "NA":
                                st.markdown(f"**Misconception:** {misconception}")
                            else:
                                st.markdown(f"**Misconception:** No aplica")

                        with col3:
                            if idx == 1:
                                st.success("Más probable")

                        st.divider()

                except FileNotFoundError as e:
                    st.error(f"Error al cargar modelos: {e}")
                    st.info("Asegúrese de que los modelos estén entrenados y guardados en las rutas correctas.")
                except Exception as e:
                    st.error(f"Error durante la clasificación: {e}")
                    st.exception(e)

with tab1:
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=fce866ce-b39f-448f-a290-d1b294affaa5&autoAuth=true&ctid=73c3e337-a317-4624-bb03-047663c4d9ed"
    st.markdown("### Dashboard Interactivo")
    components.iframe(powerbi_url, height=800, scrolling=True)

with tab2:
    st.markdown("### Resultados por Algoritmo")

    metrics_meta, metrics_df = load_algorithm_metrics()

    if metrics_meta is None or metrics_df is None or metrics_df.empty:
        st.info(
            "No se encontraron métricas pre-calculadas. "
            "Ejecute el script de evaluación para generar `algorithm_metrics.json`."
        )
    else:
        metric_cols = ["accuracy", "precision", "recall", "f1"]
        updated_at = metrics_meta.get("updated_at", "N/A")
        sample_count = metrics_meta.get("num_samples", 0)

        st.caption(
            f"Última actualización: {updated_at} · Registros evaluados: {sample_count:,}"
        )

        show_performance = st.toggle(
            "Mostrar gráficas de rendimiento",
            value=True,
            help="Desactive esta opción para ocultar temporalmente las métricas y gráficas.",
        )

        if not show_performance:
            st.info("Gráficas ocultas. Active el interruptor para volver a ver los resultados.")
        else:
            available_algorithms = metrics_df["algorithm"].tolist()
            visible_algorithms = st.multiselect(
                "Algoritmos a visualizar",
                options=available_algorithms,
                default=available_algorithms,
                help="Desmarque alguno para ocultar sus métricas del dashboard.",
            )

            if not visible_algorithms:
                st.warning("Seleccione al menos un algoritmo para visualizar resultados.")
            else:
                filtered_df = (
                    metrics_df[metrics_df["algorithm"].isin(visible_algorithms)]
                    .reset_index(drop=True)
                )

                if view_mode == "Todos los algoritmos":
                    long_df = filtered_df.melt(
                        id_vars="algorithm",
                        value_vars=metric_cols,
                        var_name="metric",
                        value_name="value",
                    )
                    long_df["percentage"] = long_df["value"] * 100

                    chart = (
                        alt.Chart(long_df)
                        .mark_bar()
                        .encode(
                            x=alt.X("metric:N", title="Métrica", sort=list(metric_cols)),
                            y=alt.Y(
                                "percentage:Q",
                                title="Valor (%)",
                                scale=alt.Scale(domain=[0, 100]),
                            ),
                            color=alt.Color("algorithm:N", title="Algoritmo"),
                            tooltip=[
                                alt.Tooltip("algorithm:N", title="Algoritmo"),
                                alt.Tooltip("metric:N", title="Métrica"),
                                alt.Tooltip("percentage:Q", title="Valor (%)", format=".2f"),
                            ],
                            xOffset="algorithm:N",
                        )
                        .properties(height=360)
                    )

                    st.altair_chart(chart, use_container_width=True)

                    table_df = filtered_df.rename(columns={"algorithm": "Algoritmo"}).copy()
                    for col in metric_cols:
                        table_df[col] = table_df[col].map(lambda v: f"{v * 100:.2f}%")

                    st.dataframe(
                        table_df,
                        hide_index=True,
                        use_container_width=True,
                    )

                    best_per_metric = (
                        filtered_df.set_index("algorithm")[metric_cols].idxmax().to_dict()
                    )
                    best_message = ", ".join(
                        f"{metric.capitalize()}: {algo}" for metric, algo in best_per_metric.items()
                    )
                    st.success(f"Mejores resultados (visibles): {best_message}")
                else:
                    algorithm = st.selectbox("Seleccione el algoritmo", filtered_df["algorithm"])
                    selected = filtered_df.loc[filtered_df["algorithm"] == algorithm].iloc[0]

                    cols = st.columns(len(metric_cols))
                    for col, metric in zip(cols, metric_cols):
                        value = selected[metric] * 100
                        col.metric(metric.capitalize(), f"{value:.2f}%")

                    chart_df = pd.DataFrame(
                        {
                            "Métrica": [m.capitalize() for m in metric_cols],
                            "Valor (%)": [selected[m] * 100 for m in metric_cols],
                        }
                    )

                    chart = (
                        alt.Chart(chart_df)
                        .mark_line(point=True)
                        .encode(
                            x=alt.X("Métrica:N", title="Métrica"),
                            y=alt.Y("Valor (%):Q", title="Valor (%)", scale=alt.Scale(domain=[0, 100])),
                            tooltip=["Métrica", "Valor (%)"],
                        )
                        .properties(height=320)
                    )
                    st.altair_chart(chart, use_container_width=True)

                    st.caption(
                        "Tip: cambie al modo *Todos los algoritmos* o modifique la lista superior para comparar resultados."
                    )
