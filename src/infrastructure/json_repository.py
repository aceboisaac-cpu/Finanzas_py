import json
import os
from typing import List
from datetime import datetime
from uuid import UUID
from src.domain.transaction import Transaction, TransactionType
from src.application.repositories import TransactionRepository

class JSONTransactionRepository(TransactionRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def save(self, transaction: Transaction) -> None:
        transactions = self.get_all()
        transactions.append(transaction)
        
        data = [
            {
                "id": str(t.id),
                "amount": t.amount,
                "category": t.category,
                "type": t.type.value,
                "date": t.date.isoformat()
            }
            for t in transactions
        ]
        
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all(self) -> List[Transaction]:
        if not os.path.exists(self.file_path):
            return []
            
        with open(self.file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
                
        return [
            Transaction(
                id=UUID(t["id"]),
                amount=t["amount"],
                category=t["category"],
                type=TransactionType(t["type"]),
                date=datetime.fromisoformat(t["date"])
            )
            for t in data
        ]
