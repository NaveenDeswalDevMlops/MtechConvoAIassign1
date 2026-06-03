# Transformer Summarization Project Specification

Dataset:

CNN/DailyMail

Source:

https://huggingface.co/datasets/cnn_dailymail

---

## MODULE 1

TASK 1
Content Truncation and Cleaning

Requirements:

1. Remove HTML tags.
2. Remove malformed unicode characters.
3. Convert non-ASCII symbols.
4. Normalize whitespace.
5. Remove duplicate spaces.
6. Normalize quotation marks.

Implement context window truncation.

Maximum article length:

512 tokens

If article exceeds limit:

* Preserve article beginning
* Preserve article ending

Recommended strategy:

First 256 tokens +
Last 256 tokens

Provide explanation:

Why truncation is necessary in Transformer architectures.

---

TASK 2
Subword Tokenization

Requirements:

Train custom tokenizer on training corpus.

Tokenizer options:

* BPE
  OR
* WordPiece

Vocabulary size:

8000–16000 tokens

Required analysis:

Explain:

1. OOV problem
2. Why word-level tokenization fails
3. How subword tokenization solves rare entity handling

Examples:

* Political names
* Company names
* Geographic locations

Demonstrate:

Tokenizer vocabulary examples.

Implement:

Dynamic padding during batching.

Batch padding must pad only to longest sequence in batch.

---

## MODULE 2

TASK 3
Encoder Decoder Construction

Implement from scratch:

Encoder Block

Components:

1. Multi-head self-attention
2. Feed-forward network
3. Layer normalization
4. Residual connections

Decoder Block

Components:

1. Masked self-attention
2. Cross-attention
3. Feed-forward network
4. Layer normalization
5. Residual connections

Cross-attention must:

Query:

Decoder hidden states

Keys:

Encoder outputs

Values:

Encoder outputs

Provide tensor shape explanation.

---

TASK 4
Masking

Implement:

Padding Mask

Purpose:

Prevent attention over PAD tokens.

Shape:

(batch_size, 1, 1, source_length)

Implement:

Causal Mask

Purpose:

Prevent future token visibility.

Shape:

(target_length, target_length)

Upper triangular masking required.

Demonstrate masks visually using heatmaps.

---

## MODULE 3

TASK 5
Training Loop

Implement teacher forcing.

Teacher forcing workflow:

Input:

<BOS> summary tokens

Target:

Shifted summary tokens

Loss:

Cross Entropy Loss

Include:

Label Smoothing

Label smoothing factor:

0.1

Training requirements:

* Forward pass
* Backward pass
* Optimizer step
* Learning rate scheduling

Train minimum:

3 epochs

Track:

* Training loss
* Validation loss

Provide loss curves.

---

TASK 6
Inference and Evaluation

Implement greedy decoding.

Generation process:

1. Start with BOS token
2. Generate next token
3. Append token
4. Continue until EOS token

Maximum summary length:

64 tokens

Evaluate on:

At least 5 unseen articles

Compute:

* ROUGE-1
* ROUGE-2
* ROUGE-L

For each article report:

1. Original article snippet
2. Reference summary
3. Generated summary

Qualitative analysis required.

Discuss:

* Repetition errors
* Missing information
* Hallucinations
* Incomplete summaries
