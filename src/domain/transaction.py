from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

# =============================================================================
# BLOQUE 1: DEFINICIÓN DE TIPOS (ENUMS)
# =============================================================================
# Usamos Enum para evitar errores de escritura. En lugar de usar strings "gasto"
# o "ingreso" que se pueden tipear mal, usamos constantes.
class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

# =============================================================================
# BLOQUE 2: LA ENTIDAD (CORAZÓN DEL NEGOCIO)
# =============================================================================
# @dataclass es un decorador de Python que nos ahorra escribir el __init__.
# Automáticamente crea el constructor y asigna los valores a self.
@dataclass
class Transaction:
    amount: float            # Monto monetario (admite decimales)
    category: str           # Nombre de la categoría (ej: "Comida")
    type: TransactionType   # Tipo: INCOME o EXPENSE (del Enum de arriba)
    
    # field(default_factory=...) se usa para dar valores por defecto que se 
    # generan en el momento. Si no proveemos una fecha, usa la actual.
    date: datetime = field(default_factory=datetime.now)
    
    # Si no proveemos un ID, genera un UUID (un identificador único mundial).
    id: UUID = field(default_factory=uuid4)

    # =========================================================================
    # BLOQUE 3: EL GUARDIÁN (POST-INICIALIZACIÓN)
    # =========================================================================
    # Este método se ejecuta automáticamente DESPUÉS de que se crea el objeto.
    # Es el lugar perfecto para poner las REGLAS DE ORO de tu negocio.
    def __post_init__(self):
        # REGLA 1: No permitimos montos negativos. 
        # Si el usuario o el archivo JSON trae un monto < 0, el programa se frena.
        if self.amount < 0:
            raise ValueError("El monto no puede ser negativo")
        
        # REGLA 2: La categoría no puede estar vacía.
        # strip() elimina los espacios en blanco sobrantes.
        if len(self.category.strip()) == 0:
            raise ValueError("La categoría no puede estar vacía")

# CONCEPTO CLAVE: Este archivo NO sabe nada de archivos JSON ni de pantallas.
# Es lógica pura. Si entendés esto, estás entendiendo el Dominio de tu App.
