"""Greedy decoding for summary generation."""

from __future__ import annotations

import torch

from .preprocessing import clean_and_truncate
from .tokenizer_utils import encode_text


def greedy_decode(
    model: torch.nn.Module,
    tokenizer,
    article: str,
    bos_id: int,
    eos_id: int,
    pad_id: int,
    max_article_tokens: int = 512,
    max_summary_tokens: int = 64,
    device: torch.device | None = None,
) -> str:
    """Generate a summary by repeatedly selecting the highest-probability token."""
    del pad_id  # pad id is held by the model; argument documents decoding contract.
    device = device or next(model.parameters()).device
    model.eval()
    cleaned_article = clean_and_truncate(article, max_article_tokens)
    source_ids = encode_text(tokenizer, cleaned_article, eos_id=eos_id, max_length=max_article_tokens)
    source_tensor = torch.tensor([source_ids], dtype=torch.long, device=device)
    generated = torch.tensor([[bos_id]], dtype=torch.long, device=device)
    with torch.no_grad():
        for _ in range(max_summary_tokens - 1):
            logits = model(source_tensor, generated)
            next_id = int(torch.argmax(logits[:, -1, :], dim=-1).item())
            generated = torch.cat(
                [generated, torch.tensor([[next_id]], dtype=torch.long, device=device)],
                dim=1,
            )
            if next_id == eos_id:
                break
    token_ids = [int(token) for token in generated.squeeze(0).tolist() if token not in {bos_id, eos_id}]
    return tokenizer.decode(token_ids).strip()
