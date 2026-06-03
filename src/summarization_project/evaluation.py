"""ROUGE scoring and qualitative evaluation helpers."""

from __future__ import annotations

from collections import Counter
from typing import Iterable


def _tokens(text: str) -> list[str]:
    return text.lower().split()


def _ngram_counts(tokens: list[str], n: int) -> Counter[tuple[str, ...]]:
    return Counter(tuple(tokens[index : index + n]) for index in range(max(0, len(tokens) - n + 1)))


def _f1(overlap: int, prediction_total: int, reference_total: int) -> float:
    if overlap == 0 or prediction_total == 0 or reference_total == 0:
        return 0.0
    precision = overlap / prediction_total
    recall = overlap / reference_total
    return 2 * precision * recall / (precision + recall)


def _rouge_n(prediction: str, reference: str, n: int) -> float:
    pred_counts = _ngram_counts(_tokens(prediction), n)
    ref_counts = _ngram_counts(_tokens(reference), n)
    overlap = sum((pred_counts & ref_counts).values())
    return _f1(overlap, sum(pred_counts.values()), sum(ref_counts.values()))


def _lcs_length(a_tokens: list[str], b_tokens: list[str]) -> int:
    previous = [0] * (len(b_tokens) + 1)
    for token_a in a_tokens:
        current = [0]
        for index_b, token_b in enumerate(b_tokens, start=1):
            if token_a == token_b:
                current.append(previous[index_b - 1] + 1)
            else:
                current.append(max(previous[index_b], current[-1]))
        previous = current
    return previous[-1]


def _rouge_l(prediction: str, reference: str) -> float:
    pred_tokens = _tokens(prediction)
    ref_tokens = _tokens(reference)
    return _f1(_lcs_length(pred_tokens, ref_tokens), len(pred_tokens), len(ref_tokens))


def compute_rouge(predictions: Iterable[str], references: Iterable[str]) -> dict[str, float]:
    """Compute average ROUGE-1, ROUGE-2, and ROUGE-L F1 scores.

    The function uses rouge-score when installed and a transparent pure-Python
    fallback otherwise so that the notebook remains runnable in constrained
    environments.
    """
    predictions = list(predictions)
    references = list(references)
    try:
        from rouge_score import rouge_scorer

        scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
        totals = {"rouge1": 0.0, "rouge2": 0.0, "rougeL": 0.0}
        for prediction, reference in zip(predictions, references):
            scores = scorer.score(reference, prediction)
            for key in totals:
                totals[key] += scores[key].fmeasure
        return {key: value / max(len(predictions), 1) for key, value in totals.items()}
    except ImportError:
        return {
            "rouge1": sum(_rouge_n(prediction, reference, 1) for prediction, reference in zip(predictions, references))
            / max(len(predictions), 1),
            "rouge2": sum(_rouge_n(prediction, reference, 2) for prediction, reference in zip(predictions, references))
            / max(len(predictions), 1),
            "rougeL": sum(_rouge_l(prediction, reference) for prediction, reference in zip(predictions, references))
            / max(len(predictions), 1),
        }
