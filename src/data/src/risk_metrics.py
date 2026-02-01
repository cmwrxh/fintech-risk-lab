from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Transaction:
    customer_id: int
    amount: float
    txn_type: str
    channel: str


def suspicious_withdrawal_ratio(transactions: Iterable[Transaction]) -> float:
    """
    Simple risk heuristic.

    Computes:
        ratio = total_withdrawals / (total_deposits + total_withdrawals)

    Returns 0.0 if there is no activity.
    """
    deposits = 0.0
    withdrawals = 0.0

    for txn in transactions:
        if txn.amount >= 0:
            deposits += txn.amount
        else:
            withdrawals += abs(txn.amount)

    total = deposits + withdrawals
    return 0.0 if total == 0 else withdrawals / total
