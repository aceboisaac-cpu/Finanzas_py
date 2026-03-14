import unittest
import os
import json
from datetime import datetime
from uuid import UUID
from domain.transaction import Transaction, TransactionType
from infrastructure.json_repository import JSONTransactionRepository

class TestJSONTransactionRepository(unittest.TestCase):
    def setUp(self):
        self.test_file = "tests/test_data.json"
        self.repository = JSONTransactionRepository(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_all(self):
        # 1. Crear una transacción
        transaction = Transaction(
            amount=150.0,
            category="Supermercado",
            type=TransactionType.EXPENSE,
            date=datetime(2026, 3, 14, 12, 0, 0)
        )

        # 2. Guardarla
        self.repository.save(transaction)

        # 3. Recuperar todas
        all_transactions = self.repository.get_all()

        # 4. Verificar
        self.assertEqual(len(all_transactions), 1)
        saved = all_transactions[0]
        self.assertEqual(saved.amount, 150.0)
        self.assertEqual(saved.category, "Supermercado")
        self.assertEqual(saved.type, TransactionType.EXPENSE)
        self.assertEqual(saved.date, datetime(2026, 3, 14, 12, 0, 0))
        self.assertIsInstance(saved.id, UUID)

if __name__ == '__main__':
    unittest.main()
