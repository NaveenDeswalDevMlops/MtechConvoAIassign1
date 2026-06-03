"""Dataset loading and batching helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import torch
from torch.utils.data import DataLoader, Dataset

from .config import ExperimentConfig, SpecialTokens
from .preprocessing import clean_and_truncate, clean_text
from .tokenizer_utils import dynamic_pad, encode_text, token_id


@dataclass
class ArticleSummaryExample:
    """Cleaned article-summary pair."""

    article: str
    summary: str


class SummarizationDataset(Dataset):
    """Tokenized article-summary dataset with teacher-forcing fields."""

    def __init__(self, examples: list[ArticleSummaryExample], tokenizer: Any, config: ExperimentConfig):
        self.examples = examples
        self.tokenizer = tokenizer
        self.config = config
        specials = SpecialTokens()
        self.bos_id = token_id(tokenizer, specials.bos)
        self.eos_id = token_id(tokenizer, specials.eos)

    def __len__(self) -> int:
        return len(self.examples)

    def __getitem__(self, index: int) -> dict[str, Any]:
        example = self.examples[index]
        source_ids = encode_text(
            self.tokenizer,
            example.article,
            eos_id=self.eos_id,
            max_length=self.config.max_article_tokens,
        )
        summary_ids = encode_text(
            self.tokenizer,
            example.summary,
            bos_id=self.bos_id,
            eos_id=self.eos_id,
            max_length=self.config.max_summary_tokens,
        )
        return {
            "source_ids": source_ids,
            "decoder_input_ids": summary_ids[:-1],
            "target_ids": summary_ids[1:],
            "article": example.article,
            "summary": example.summary,
        }


def collate_batch(batch: list[dict[str, Any]], pad_id: int) -> dict[str, Any]:
    """Dynamically pad source, decoder input, and target tensors per batch."""
    source_ids, source_lengths = dynamic_pad([item["source_ids"] for item in batch], pad_id)
    decoder_ids, decoder_lengths = dynamic_pad([item["decoder_input_ids"] for item in batch], pad_id)
    target_ids, _ = dynamic_pad([item["target_ids"] for item in batch], pad_id)
    return {
        "source_ids": torch.tensor(source_ids, dtype=torch.long),
        "decoder_input_ids": torch.tensor(decoder_ids, dtype=torch.long),
        "target_ids": torch.tensor(target_ids, dtype=torch.long),
        "source_lengths": source_lengths,
        "decoder_lengths": decoder_lengths,
        "articles": [item["article"] for item in batch],
        "summaries": [item["summary"] for item in batch],
    }


def make_dataloader(dataset: SummarizationDataset, pad_id: int, batch_size: int, shuffle: bool) -> DataLoader:
    """Create a PyTorch DataLoader using dynamic padding."""
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        collate_fn=lambda batch: collate_batch(batch, pad_id=pad_id),
    )


def load_cnn_dailymail_splits(config: ExperimentConfig) -> tuple[list[ArticleSummaryExample], ...]:
    """Download CNN/DailyMail and return small deterministic train/val/test splits."""
    try:
        from datasets import load_dataset
    except ImportError as exc:  # pragma: no cover
        raise ImportError("Install datasets with `pip install datasets`.") from exc

    raw = load_dataset(config.dataset_name, config.dataset_config)

    def convert(split_name: str, count: int) -> list[ArticleSummaryExample]:
        rows = raw[split_name].select(range(count))
        return [
            ArticleSummaryExample(
                article=clean_and_truncate(row["article"], config.max_article_tokens),
                summary=clean_text(row["highlights"]),
            )
            for row in rows
        ]

    return (
        convert("train", config.train_subset_size),
        convert("validation", config.val_subset_size),
        convert("test", config.test_subset_size),
    )
