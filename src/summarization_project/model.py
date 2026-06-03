"""Transformer encoder-decoder implemented from scratch in PyTorch."""

from __future__ import annotations

import math

import torch
from torch import nn


class PositionalEncoding(nn.Module):
    """Sinusoidal positional encoding added to token embeddings."""

    def __init__(self, d_model: int, max_length: int = 2048, dropout: float = 0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        positions = torch.arange(max_length, dtype=torch.float).unsqueeze(1)
        div_terms = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        encodings = torch.zeros(max_length, d_model)
        encodings[:, 0::2] = torch.sin(positions * div_terms)
        encodings[:, 1::2] = torch.cos(positions * div_terms)
        self.register_buffer("encodings", encodings.unsqueeze(0), persistent=False)

    def forward(self, embeddings: torch.Tensor) -> torch.Tensor:
        """Add positional encodings to embeddings shaped (batch, seq, d_model)."""
        return self.dropout(embeddings + self.encodings[:, : embeddings.size(1)])


class MultiHeadAttention(nn.Module):
    """Explicit multi-head attention implemented with custom projections."""

    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.query_projection = nn.Linear(d_model, d_model)
        self.key_projection = nn.Linear(d_model, d_model)
        self.value_projection = nn.Linear(d_model, d_model)
        self.output_projection = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)
        self.last_attention_weights: torch.Tensor | None = None

    def split_heads(self, tensor: torch.Tensor) -> torch.Tensor:
        """Convert (batch, seq, d_model) to (batch, heads, seq, head_dim)."""
        batch_size, seq_length, _ = tensor.shape
        tensor = tensor.view(batch_size, seq_length, self.num_heads, self.head_dim)
        return tensor.transpose(1, 2)

    def concatenate_heads(self, tensor: torch.Tensor) -> torch.Tensor:
        """Convert (batch, heads, seq, head_dim) back to (batch, seq, d_model)."""
        batch_size, _, seq_length, _ = tensor.shape
        tensor = tensor.transpose(1, 2).contiguous()
        return tensor.view(batch_size, seq_length, self.d_model)

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        """Compute softmax(QK^T / sqrt(d_k))V with optional boolean mask."""
        q_heads = self.split_heads(self.query_projection(query))
        k_heads = self.split_heads(self.key_projection(key))
        v_heads = self.split_heads(self.value_projection(value))
        scores = torch.matmul(q_heads, k_heads.transpose(-2, -1)) / math.sqrt(self.head_dim)
        if mask is not None:
            scores = scores.masked_fill(~mask, torch.finfo(scores.dtype).min)
        attention_weights = torch.softmax(scores, dim=-1)
        self.last_attention_weights = attention_weights.detach()
        context = torch.matmul(self.dropout(attention_weights), v_heads)
        return self.output_projection(self.concatenate_heads(context))


class FeedForwardNetwork(nn.Module):
    """Position-wise Transformer feed-forward network."""

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.layers(inputs)


class EncoderBlock(nn.Module):
    """Transformer encoder block with self-attention, residuals, and layer norm."""

    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm_attention = nn.LayerNorm(d_model)
        self.norm_ffn = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, inputs: torch.Tensor, source_mask: torch.Tensor | None) -> torch.Tensor:
        attention = self.self_attention(inputs, inputs, inputs, source_mask)
        outputs = self.norm_attention(inputs + self.dropout(attention))
        ffn_outputs = self.feed_forward(outputs)
        return self.norm_ffn(outputs + self.dropout(ffn_outputs))


class DecoderBlock(nn.Module):
    """Transformer decoder block with masked self-attention and cross-attention."""

    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.masked_self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.cross_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm_self = nn.LayerNorm(d_model)
        self.norm_cross = nn.LayerNorm(d_model)
        self.norm_ffn = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        inputs: torch.Tensor,
        encoder_outputs: torch.Tensor,
        target_mask: torch.Tensor | None,
        source_mask: torch.Tensor | None,
    ) -> torch.Tensor:
        self_attention = self.masked_self_attention(inputs, inputs, inputs, target_mask)
        outputs = self.norm_self(inputs + self.dropout(self_attention))
        cross_attention = self.cross_attention(outputs, encoder_outputs, encoder_outputs, source_mask)
        outputs = self.norm_cross(outputs + self.dropout(cross_attention))
        ffn_outputs = self.feed_forward(outputs)
        return self.norm_ffn(outputs + self.dropout(ffn_outputs))


class TransformerSummarizer(nn.Module):
    """Encoder-decoder Transformer for abstractive summarization."""

    def __init__(
        self,
        vocab_size: int,
        pad_id: int,
        d_model: int = 128,
        num_heads: int = 4,
        d_ff: int = 512,
        num_layers: int = 2,
        dropout: float = 0.1,
        max_length: int = 1024,
    ):
        super().__init__()
        self.pad_id = pad_id
        self.d_model = d_model
        self.source_embedding = nn.Embedding(vocab_size, d_model, padding_idx=pad_id)
        self.target_embedding = nn.Embedding(vocab_size, d_model, padding_idx=pad_id)
        self.positional_encoding = PositionalEncoding(d_model, max_length=max_length, dropout=dropout)
        self.encoder_layers = nn.ModuleList(
            [EncoderBlock(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.decoder_layers = nn.ModuleList(
            [DecoderBlock(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.output_projection = nn.Linear(d_model, vocab_size)

    @staticmethod
    def make_padding_mask(tokens: torch.Tensor, pad_id: int) -> torch.Tensor:
        """Return mask shaped (batch_size, 1, 1, sequence_length)."""
        return (tokens != pad_id).unsqueeze(1).unsqueeze(2)

    @staticmethod
    def make_causal_mask(length: int, device: torch.device) -> torch.Tensor:
        """Return upper-triangular causal visibility mask shaped (length, length)."""
        return torch.tril(torch.ones((length, length), dtype=torch.bool, device=device))

    def encode(self, source_ids: torch.Tensor, source_mask: torch.Tensor) -> torch.Tensor:
        """Encode source ids into contextual states."""
        outputs = self.source_embedding(source_ids) * math.sqrt(self.d_model)
        outputs = self.positional_encoding(outputs)
        for layer in self.encoder_layers:
            outputs = layer(outputs, source_mask)
        return outputs

    def decode(
        self,
        decoder_input_ids: torch.Tensor,
        encoder_outputs: torch.Tensor,
        source_mask: torch.Tensor,
    ) -> torch.Tensor:
        """Decode with causal self-attention and encoder-output cross-attention."""
        target_length = decoder_input_ids.size(1)
        padding_mask = self.make_padding_mask(decoder_input_ids, self.pad_id)
        causal_mask = self.make_causal_mask(target_length, decoder_input_ids.device).unsqueeze(0).unsqueeze(0)
        target_mask = padding_mask & causal_mask
        outputs = self.target_embedding(decoder_input_ids) * math.sqrt(self.d_model)
        outputs = self.positional_encoding(outputs)
        for layer in self.decoder_layers:
            outputs = layer(outputs, encoder_outputs, target_mask, source_mask)
        return outputs

    def forward(self, source_ids: torch.Tensor, decoder_input_ids: torch.Tensor) -> torch.Tensor:
        """Return token logits shaped (batch, target_length, vocab_size)."""
        source_mask = self.make_padding_mask(source_ids, self.pad_id)
        encoder_outputs = self.encode(source_ids, source_mask)
        decoder_outputs = self.decode(decoder_input_ids, encoder_outputs, source_mask)
        return self.output_projection(decoder_outputs)
