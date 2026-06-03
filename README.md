# Transformer Summarization Assignment

This repository contains a complete from-scratch abstractive text summarization project for CNN/DailyMail using PyTorch. It implements a custom encoder-decoder Transformer rather than relying on pretrained or prebuilt Transformer summarization models.

## Delivered Files

- `transformer_summarization.ipynb` — end-to-end notebook with the required nine sections.
- `report.pdf` — assignment report covering the required methodology and analysis topics.
- `README.md` — setup, run, and grading checklist.
- `train.py` — reproducible script entry point for the same pipeline.
- `src/summarization_project/` — modular production-quality implementation.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

The code uses seed `42` for Python, NumPy, PyTorch CPU, and PyTorch CUDA reproducibility.

## Run End to End

### Notebook

Open `transformer_summarization.ipynb` and select **Run All**. The notebook downloads CNN/DailyMail, trains the BPE tokenizer, trains the Transformer for three epochs, runs greedy decoding, and reports ROUGE on five unseen test examples.

### Script

```bash
python train.py
```

Optional CPU-friendly overrides:

```bash
python train.py --train-size 64 --val-size 16 --test-size 5 --epochs 3 --batch-size 4
```

## Architecture Summary

The model in `src/summarization_project/model.py` implements:

- token embeddings and sinusoidal positional encodings;
- explicit multi-head attention with query, key, and value projections;
- head splitting and concatenation;
- encoder self-attention blocks;
- decoder masked self-attention blocks;
- decoder-to-encoder cross-attention where decoder states are queries and encoder outputs are keys/values;
- feed-forward networks;
- residual connections;
- layer normalization;
- padding masks and causal masks.

The implementation intentionally does **not** use PyTorch built-in multi-head attention, Hugging Face seq2seq auto-models, T5, BART, Pegasus, GPT, or any pretrained Transformer summarization model.

## Preprocessing and Tokenization

`src/summarization_project/preprocessing.py` removes HTML tags, malformed unicode, non-ASCII symbols, duplicate spaces, and normalizes quotation marks. Articles longer than 512 whitespace tokens are truncated with a context-window strategy: the first 256 tokens plus the last 256 tokens.

`src/summarization_project/tokenizer_utils.py` trains a custom BPE tokenizer on the training corpus. The default vocabulary size is 8,000 tokens, satisfying the required 8,000-16,000 range. Dynamic padding is implemented in `src/summarization_project/data.py` so each batch pads only to the longest sequence in that batch.

## Training and Evaluation

Training uses teacher forcing:

- decoder input: `<BOS>` followed by summary tokens;
- target: shifted summary tokens ending in `<EOS>`;
- loss: cross entropy with label smoothing factor `0.1`;
- optimizer: AdamW;
- scheduler: StepLR;
- minimum epochs: three.

Evaluation uses greedy decoding with a maximum generated summary length of 64 tokens and computes ROUGE-1, ROUGE-2, and ROUGE-L for at least five unseen test articles.

## Grading Checklist

- [x] CNN/DailyMail dataset loading
- [x] Data cleaning and context-window truncation
- [x] Custom BPE tokenizer
- [x] Vocabulary size in 8,000-16,000 range
- [x] Dynamic batch padding
- [x] Custom multi-head attention
- [x] Custom encoder blocks
- [x] Custom decoder blocks
- [x] Custom cross-attention
- [x] Padding mask with shape `(batch_size, 1, 1, source_length)`
- [x] Causal mask with upper-triangular future masking behavior
- [x] Mask heatmap demonstration in notebook
- [x] Teacher forcing
- [x] Label smoothing `0.1`
- [x] Training and validation loss tracking
- [x] Loss curves in notebook
- [x] Greedy decoding
- [x] ROUGE-1, ROUGE-2, ROUGE-L evaluation
- [x] Generated summaries for five unseen articles
- [x] Qualitative/error analysis
- [x] Reproducible `python train.py` entry point
