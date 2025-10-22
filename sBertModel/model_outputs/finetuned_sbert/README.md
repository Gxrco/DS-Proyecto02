---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:2526
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: 'What fraction of the shape is not shaded? Give your answer in
    its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6
    of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: I think this is because
    3/9 is not shaded. If you divide 3 by 3 it equals 1/3.'
  sentences:
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: The answer is because the fraction that
    is not shaded is 3/9 but since your meant to have it in it''s simplest form the
    correct answer would be 1/3'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: I found out what the dominant was then
    looked at the partss that were not shaded in and that was 3.'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: Because there are 9 triangle all together
    and 3 have been shaded but if you simplify it ,it will become1/3'
- source_sentence: 'What fraction of the shape is not shaded? Give your answer in
    its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6
    of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: 3 out of nine triangles
    are not shaded'
  sentences:
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: because 6/9 are shaded and there are 3/9
    remaining.'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: there is a common factor of 3 in 3/9'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: there is 9 triangles and 3 are not shaded'
- source_sentence: 'What fraction of the shape is not shaded? Give your answer in
    its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6
    of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: its (A) because if
    you simplify 3/9 then you get 1/3'
  sentences:
  - 'Calculate \( \frac{1}{2} \div 6 \) Answer: \( 3 \) Explanation: Because half
    of six is 3'
  - 'Calculate \( \frac{1}{2} \div 6 \) Answer: \( 3 \) Explanation: Because of half
    of six equals three'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: There are 3 unshaded out of 9 and simplify
    that and it is 1/3'
- source_sentence: 'What fraction of the shape is not shaded? Give your answer in
    its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6
    of them are shaded.] Answer: \( \frac{3}{9} \) Explanation: because you count
    the number of triangles, then count the amount of shaded triangles'
  sentences:
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{3}{9} \) Explanation: The answer is because the fraction that
    is not shaded is 3/9 but since your meant to have it in it''s simplest form the
    correctt answer would be 1/3.'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: The answer is A 1/2 because 3/9 simplified
    is 1/2.'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: I think this because there are 9 parts
    and there are 3 that have not been shaded in, so you get 3/9. Then, simplified,
    it is 1/3, for 3 goes into 3 and 9.'
- source_sentence: 'What fraction of the shape is not shaded? Give your answer in
    its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6
    of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: i know this because
    there is 6 triangles shaded and 3 are not shaded so 3/9 also equals 1/3 and that
    is its simplest form'
  sentences:
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: because you can simplify 6 ninths to 3
    sixths and then 1 third'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: There are nott 3 shaded in, so it would
    be 1/3.'
  - 'What fraction of the shape is not shaded? Give your answer in its simplest form.
    [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.]
    Answer: \( \frac{1}{3} \) Explanation: One third is three little triangles.'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: validation
      type: validation
    metrics:
    - type: pearson_cosine
      value: .nan
      name: Pearson Cosine
    - type: spearman_cosine
      value: .nan
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \\( \\frac{1}{3} \\) Explanation: i know this because there is 6 triangles shaded and 3 are not shaded so 3/9 also equals 1/3 and that is its simplest form',
    'What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \\( \\frac{1}{3} \\) Explanation: There are nott 3 shaded in, so it would be 1/3.',
    'What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \\( \\frac{1}{3} \\) Explanation: because you can simplify 6 ninths to 3 sixths and then 1 third',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.7640, 0.8163],
#         [0.7640, 1.0000, 0.7073],
#         [0.8163, 0.7073, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Dataset: `validation`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value   |
|:--------------------|:--------|
| pearson_cosine      | nan     |
| **spearman_cosine** | **nan** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 2,526 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          | label                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              | float                                                          |
  | details | <ul><li>min: 35 tokens</li><li>mean: 73.08 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 35 tokens</li><li>mean: 73.38 tokens</li><li>max: 115 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.42</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | sentence_1                                                                                                                                                                                                                                                                                         | label            |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: the answer is 3 but it can be simplified to 1 and 9.</code>                                                                                                                                                                                                                   | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{3}{9} \) Explanation: because 6/9 are shaded and there are 3/9 remaining.</code>                           | <code>0.0</code> |
  | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{3}{9} \) Explanation: 3 out of thee 9 are not shaded</code>                                                                                                                                                                                                                                         | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{3}{9} \) Explanation: there sre 9 squares and 3 are not shaded so 9 divided by 3 = 3 so it is 1 / 3</code> | <code>0.0</code> |
  | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: altogether there are 9 triangles and 3 of which are not shaded, so that means that 3/9 are not shaded. Once you have figured out what fraction is NOT shaded, you can simplify, by dividing both the numerator and the denominator by 3 so your new answer will be 1/3</code> | <code>What fraction of the shape is not shaded? Give your answer in its simplest form. [Image: A triangle split into 9 equal smaller triangles. 6 of them are shaded.] Answer: \( \frac{1}{3} \) Explanation: A is the correct answer because the the simplest form of the shape is 1/3</code>     | <code>0.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | validation_spearman_cosine |
|:------:|:----:|:--------------------------:|
| 0.6329 | 100  | nan                        |


### Framework Versions
- Python: 3.10.2
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.9.0
- Accelerate: 1.11.0
- Datasets: 4.2.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->