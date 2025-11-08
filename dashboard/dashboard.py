import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
import warnings

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

tab1, tab2 = st.tabs(["Clasificación de Explicaciones", "Dashboard Interactivo"])

with tab1:
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
                    else:  # MLP
                        category_model = load_model(MODEL_OUTPUTS_DIR / "category_model_mlp.pkl")

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

with tab2:
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=fce866ce-b39f-448f-a290-d1b294affaa5&autoAuth=true&ctid=73c3e337-a317-4624-bb03-047663c4d9ed"
    st.markdown("### Dashboard Interactivo")
    components.iframe(powerbi_url, height=800, scrolling=True)
