# Transformer Summarization Assignment - Agent Specification

## Objective

Build a complete Transformer-based abstractive text summarization system from scratch using PyTorch.

The implementation must cover:

1. Document preprocessing
2. Custom tokenizer training
3. Encoder architecture
4. Decoder architecture
5. Cross-attention mechanism
6. Padding masks
7. Causal masks
8. Teacher forcing training
9. Label smoothing
10. Greedy decoding
11. ROUGE evaluation

Prebuilt Transformer models are NOT allowed.

Examples of prohibited models:

* T5
* BART
* Pegasus
* GPT
* MarianMT
* Any HuggingFace AutoModelForSeq2SeqLM

Allowed:

* PyTorch tensors
* PyTorch autograd
* Custom implementation of attention layers
* Custom encoder-decoder architecture

## Framework

Primary Framework:

* PyTorch

Optional:

* NumPy
* Pandas
* Matplotlib
* NLTK
* evaluate
* rouge-score
* tokenizers

## Coding Standards

All code must:

* Be modular
* Contain comments
* Follow PEP8 style
* Use reproducible random seeds

Required seed:

42

## Architecture Requirements

Must implement:

### Encoder

* Token Embeddings
* Positional Encoding
* Multi-head Self-Attention
* Feed Forward Network
* Layer Normalization
* Residual Connections

### Decoder

* Token Embeddings
* Positional Encoding
* Masked Self-Attention
* Cross-Attention
* Feed Forward Network
* Layer Normalization
* Residual Connections

### Attention

Attention score computation:

Softmax(QKᵀ / √d)

Must explicitly implement:

* Query projection
* Key projection
* Value projection
* Head splitting
* Head concatenation

No use of torch.nn.MultiheadAttention.

## Evaluation Rules

Evaluate on at least:

* 5 unseen test articles

Report:

* ROUGE-1
* ROUGE-2
* ROUGE-L

Include qualitative analysis.

## Reproducibility

All outputs must be reproducible using:

python train.py

or

Run All in notebook.
