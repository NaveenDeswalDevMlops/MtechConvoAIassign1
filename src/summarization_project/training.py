"""Training loop with teacher forcing and label smoothing."""

from __future__ import annotations

import random
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
from torch import nn

from .config import ExperimentConfig


def set_seed(seed: int = 42) -> None:
    """Set all practical seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def make_label_smoothed_loss(pad_id: int, smoothing: float = 0.1) -> nn.CrossEntropyLoss:
    """Create cross entropy loss with assignment-required label smoothing."""
    return nn.CrossEntropyLoss(ignore_index=pad_id, label_smoothing=smoothing)


def run_epoch(
    model: nn.Module,
    dataloader: Iterable[dict[str, torch.Tensor]],
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer | None,
    device: torch.device,
) -> float:
    """Run one training or validation epoch."""
    is_training = optimizer is not None
    model.train(is_training)
    total_loss = 0.0
    total_batches = 0
    for batch in dataloader:
        source_ids = batch["source_ids"].to(device)
        decoder_input_ids = batch["decoder_input_ids"].to(device)
        target_ids = batch["target_ids"].to(device)
        if is_training:
            optimizer.zero_grad(set_to_none=True)
        logits = model(source_ids, decoder_input_ids)
        loss = criterion(logits.reshape(-1, logits.size(-1)), target_ids.reshape(-1))
        if is_training:
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
        total_loss += loss.item()
        total_batches += 1
    return total_loss / max(total_batches, 1)


def train_model(
    model: nn.Module,
    train_loader: Iterable[dict[str, torch.Tensor]],
    val_loader: Iterable[dict[str, torch.Tensor]],
    pad_id: int,
    config: ExperimentConfig,
    device: torch.device,
) -> dict[str, list[float]]:
    """Train for at least three epochs with AdamW and step LR scheduling."""
    criterion = make_label_smoothed_loss(pad_id, config.label_smoothing)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(
        optimizer,
        step_size=config.scheduler_step_size,
        gamma=config.scheduler_gamma,
    )
    history = {"train_loss": [], "val_loss": []}
    for epoch in range(config.epochs):
        train_loss = run_epoch(model, train_loader, criterion, optimizer, device)
        val_loss = run_epoch(model, val_loader, criterion, None, device)
        scheduler.step()
        history["train_loss"].append(train_loss)
        history["val_loss"].append(val_loss)
        print(f"Epoch {epoch + 1}/{config.epochs}: train={train_loss:.4f}, val={val_loss:.4f}")
    checkpoint_path = Path(config.checkpoint_path)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state_dict": model.state_dict(), "history": history}, checkpoint_path)
    return history
