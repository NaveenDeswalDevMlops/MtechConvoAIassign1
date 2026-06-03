"""Custom BPE tokenizer training and dynamic padding."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

try:
    from tokenizers import Tokenizer
    from tokenizers.decoders import BPEDecoder
    from tokenizers.models import BPE
    from tokenizers.pre_tokenizers import Whitespace
    from tokenizers.trainers import BpeTrainer
except ImportError as exc:  # pragma: no cover - dependency guard for users
    raise ImportError(
        "Install tokenizers with `pip install tokenizers` to train the custom BPE tokenizer."
    ) from exc

from .config import SpecialTokens


def train_bpe_tokenizer(
    texts: Sequence[str],
    output_path: str | Path,
    vocab_size: int = 8000,
    min_frequency: int = 2,
    special_tokens: SpecialTokens | None = None,
) -> Tokenizer:
    """Train a custom BPE tokenizer on the supplied training corpus."""
    special_tokens = special_tokens or SpecialTokens()
    tokenizer = Tokenizer(BPE(unk_token=special_tokens.unk))
    tokenizer.pre_tokenizer = Whitespace()
    tokenizer.decoder = BPEDecoder()
    trainer = BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=special_tokens.all,
        show_progress=True,
    )
    tokenizer.train_from_iterator(texts, trainer=trainer)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tokenizer.save(str(output_path))
    return tokenizer


def load_tokenizer(path: str | Path) -> Tokenizer:
    """Load a previously trained tokenizer."""
    tokenizer = Tokenizer.from_file(str(path))
    tokenizer.decoder = BPEDecoder()
    return tokenizer


def token_id(tokenizer: Tokenizer, token: str) -> int:
    """Return the id for a token, failing loudly if it is absent."""
    token_id_value = tokenizer.token_to_id(token)
    if token_id_value is None:
        raise ValueError(f"Tokenizer does not contain required token: {token}")
    return int(token_id_value)


def encode_text(
    tokenizer: Tokenizer,
    text: str,
    bos_id: int | None = None,
    eos_id: int | None = None,
    max_length: int | None = None,
) -> list[int]:
    """Encode text and optionally add BOS/EOS plus length clipping."""
    ids = tokenizer.encode(text).ids
    if max_length is not None:
        reserved = int(bos_id is not None) + int(eos_id is not None)
        ids = ids[: max(0, max_length - reserved)]
    if bos_id is not None:
        ids = [bos_id] + ids
    if eos_id is not None:
        ids = ids + [eos_id]
    return ids


def dynamic_pad(sequences: Sequence[Sequence[int]], pad_id: int) -> tuple[list[list[int]], list[int]]:
    """Pad only to the longest sequence in the current batch."""
    lengths = [len(sequence) for sequence in sequences]
    max_length = max(lengths) if lengths else 0
    padded = [list(sequence) + [pad_id] * (max_length - len(sequence)) for sequence in sequences]
    return padded, lengths
