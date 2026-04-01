---
name: autoresearch
description: |
  Autonomous LLM pretraining research on a single GPU. Runs automated experiments on GPT model architecture, 
  optimizer, and hyperparameters overnight. Use when: (1) User wants to run autonomous AI research experiments, 
  (2) User wants to optimize LLM training on a single GPU, (3) User wants to experiment with GPT architecture 
  changes and see results automatically, or (4) User references karpathy/autoresearch or autonomous pretraining research.
---

# Autoresearch

Autonomous LLM pretraining research. Gives an AI agent a small LLM training setup to experiment autonomously.

## Requirements

- NVIDIA GPU (tested on H100)
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

```bash
# 1. Install uv (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Download data and train tokenizer (~2 min)
uv run prepare.py
```

## Files

- `prepare.py` — Fixed constants, data prep, tokenizer (DO NOT modify)
- `train.py` — The only file the agent modifies (model, optimizer, training loop)
- `program.md` — Agent instructions

## Running

**Manual single run:**
```bash
uv run train.py
```

**Autonomous mode**: Point your agent (Claude/Codex) at `program.md` with no permissions.

## Key Constraints

- **5-minute fixed time budget** (wall clock training time)
- **Metric**: val_bpb (validation bits per byte) — lower is better
- **VRAM**: Soft constraint, some increase OK for meaningful gains
- **Simplicity**: All else equal, simpler is better

## Output

After training:
```
val_bpb:          0.997900
training_seconds: 300.1
total_seconds:    325.9
peak_vram_mb:     45060.2
```

Results are logged to `results.tsv`.