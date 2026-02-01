import csv
from pathlib import Path

from risk_metrics import Transaction, suspicious_withdrawal_ratio


def load_transactions(csv_path: Path):
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Transaction(
                customer_id=int(row["customer_id"]),
                amount=float(row["amount"]),
                txn_type=row["txn_type"],
                channel=row["channel"],
            )


if __name__ == "__main__":
    data_path = Path("data/sample_transactions.csv")
    transactions = list(load_transactions(data_path))

    ratio = suspicious_withdrawal_ratio(transactions)
    print(f"suspicious_withdrawal_ratio = {ratio:.3f}")
