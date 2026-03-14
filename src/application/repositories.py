from abc import ABC, abstractmethod
from typing import List
from domain.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        """Guarda una transacción en la persistencia."""
        pass

    @abstractmethod
    def get_all(self) -> List[Transaction]:
        """Recupera todas las transacciones de la persistencia."""
        pass
