"""Project configuration for reproducible Transformer summarization."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SpecialTokens:
    """Special tokenizer tokens shared across preprocessing and modeling."""

    pad: str = "<PAD>"
    unk: str = "<UNK>"
    bos: str = "<BOS>"
    eos: str = "<EOS>"

    @property
    def all(self) -> list[str]:
        """Return tokens in a stable order for tokenizer training."""
        return [self.pad, self.unk, self.bos, self.eos]


@dataclass
class ExperimentConfig:
    """Default settings selected to run on CPU for assignment reproducibility."""

    seed: int = 42
    dataset_name: str = "cnn_dailymail"
    dataset_config: str = "3.0.0"
    train_subset_size: int = 64
    val_subset_size: int = 16
    test_subset_size: int = 5
    max_article_tokens: int = 512
    max_summary_tokens: int = 96
    max_generated_tokens: int = 64
    vocab_size: int = 8000
    min_frequency: int = 2
    batch_size: int = 4
    epochs: int = 3
    d_model: int = 128
    num_heads: int = 4
    d_ff: int = 512
    num_layers: int = 2
    dropout: float = 0.1
    label_smoothing: float = 0.1
    learning_rate: float = 3e-4
    scheduler_step_size: int = 1
    scheduler_gamma: float = 0.95
    tokenizer_path: str = "artifacts/bpe_tokenizer.json"
    checkpoint_path: str = "artifacts/transformer_summarizer.pt"
