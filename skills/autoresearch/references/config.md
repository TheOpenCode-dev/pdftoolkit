# Autoresearch Reference

## Key Hyperparameters (in train.py)

| Parameter | Default | Description |
|-----------|---------|-------------|
| DEPTH (n_layer) | 12 | Number of transformer layers |
| n_head | 6 | Number of attention heads |
| n_embd | 768 | Embedding dimension |
| n_kv_head | 6 | Key/value heads |
| window_pattern | "SSSL" | Attention pattern (S=short, L=long) |
| vocab_size | 32768 | Vocabulary size |
| MAX_SEQ_LEN | 2048 | Context length |
| TOTAL_BATCH_SIZE | 262144 | Tokens per batch |
| DEVICE_BATCH_SIZE | 32 | Samples per device |

## Optimizer Settings

- **Muon** for matrices: lr=0.02, momentum=0.95, ns_steps=5
- **AdamW** for embeddings: lr=0.004 (unembed), 0.2 (embed)
- **Scalar params**: lr=0.5

## What to Modify

Only `train.py` is editable:
- Model architecture (attention, MLP)
- Optimizer choice and hyperparameters
- Batch size, learning rates
- Activation functions
- Normalization

## What NOT to Modify

- `prepare.py` is read-only (fixed eval, data loading)
- No new package dependencies allowed
- Evaluation harness is fixed

## Performance Tips

- Default runs on H100, ~50M parameters
- For MacBooks: reduce DEPTH to 4, vocab to 2048-4096, MAX_SEQ_LEN to 256
- Total batch size should be power of 2