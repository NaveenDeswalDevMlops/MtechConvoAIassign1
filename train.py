"""Run the Transformer summarization assignment end to end.

The script downloads CNN/DailyMail, trains a custom BPE tokenizer, trains a
from-scratch PyTorch encoder-decoder Transformer for three epochs on a small
CPU-friendly subset, and evaluates five unseen test articles with ROUGE.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import torch

from summarization_project.config import ExperimentConfig, SpecialTokens
from summarization_project.data import SummarizationDataset, load_cnn_dailymail_splits, make_dataloader
from summarization_project.evaluation import compute_rouge
from summarization_project.generation import greedy_decode
from summarization_project.model import TransformerSummarizer
from summarization_project.tokenizer_utils import load_tokenizer, token_id, train_bpe_tokenizer
from summarization_project.training import set_seed, train_model


def parse_args() -> argparse.Namespace:
    """Parse optional subset overrides for local experimentation."""
    parser = argparse.ArgumentParser(description="Train custom Transformer summarizer.")
    parser.add_argument("--train-size", type=int, default=ExperimentConfig.train_subset_size)
    parser.add_argument("--val-size", type=int, default=ExperimentConfig.val_subset_size)
    parser.add_argument("--test-size", type=int, default=ExperimentConfig.test_subset_size)
    parser.add_argument("--epochs", type=int, default=ExperimentConfig.epochs)
    parser.add_argument("--batch-size", type=int, default=ExperimentConfig.batch_size)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    return parser.parse_args()


def main() -> None:
    """Execute dataset loading, tokenizer training, model training, and evaluation."""
    args = parse_args()
    config = ExperimentConfig(
        train_subset_size=args.train_size,
        val_subset_size=args.val_size,
        test_subset_size=args.test_size,
        epochs=max(3, args.epochs),
        batch_size=args.batch_size,
    )
    set_seed(config.seed)
    train_examples, val_examples, test_examples = load_cnn_dailymail_splits(config)
    tokenizer_path = Path(config.tokenizer_path)
    if tokenizer_path.exists():
        tokenizer = load_tokenizer(tokenizer_path)
    else:
        tokenizer = train_bpe_tokenizer(
            [example.article for example in train_examples] + [example.summary for example in train_examples],
            tokenizer_path,
            vocab_size=config.vocab_size,
            min_frequency=config.min_frequency,
        )

    specials = SpecialTokens()
    pad_id = token_id(tokenizer, specials.pad)
    bos_id = token_id(tokenizer, specials.bos)
    eos_id = token_id(tokenizer, specials.eos)
    train_dataset = SummarizationDataset(train_examples, tokenizer, config)
    val_dataset = SummarizationDataset(val_examples, tokenizer, config)
    train_loader = make_dataloader(train_dataset, pad_id, config.batch_size, shuffle=True)
    val_loader = make_dataloader(val_dataset, pad_id, config.batch_size, shuffle=False)

    device = torch.device(args.device)
    model = TransformerSummarizer(
        vocab_size=tokenizer.get_vocab_size(),
        pad_id=pad_id,
        d_model=config.d_model,
        num_heads=config.num_heads,
        d_ff=config.d_ff,
        num_layers=config.num_layers,
        dropout=config.dropout,
        max_length=max(config.max_article_tokens, config.max_summary_tokens) + 8,
    ).to(device)
    history = train_model(model, train_loader, val_loader, pad_id, config, device)
    print("Training history:", history)

    predictions = []
    references = []
    for index, example in enumerate(test_examples[:5], start=1):
        generated = greedy_decode(
            model,
            tokenizer,
            example.article,
            bos_id=bos_id,
            eos_id=eos_id,
            pad_id=pad_id,
            max_article_tokens=config.max_article_tokens,
            max_summary_tokens=config.max_generated_tokens,
            device=device,
        )
        predictions.append(generated)
        references.append(example.summary)
        print(f"\nExample {index}")
        print("Article snippet:", example.article[:500])
        print("Reference:", example.summary)
        print("Generated:", generated)
    print("\nROUGE:", compute_rouge(predictions, references))


if __name__ == "__main__":
    main()
