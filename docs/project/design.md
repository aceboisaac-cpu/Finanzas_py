# Diseño: Gestor de Finanzas Personales (Expense Tracker)

## Enfoque Técnico

La aplicación CLI seguirá los principios de **Clean Architecture** (Arquitectura Limpia) para separar la lógica de negocio central de los frameworks externos (la interfaz CLI y el sistema de archivos JSON). 

Este enfoque cumple con el objetivo educativo (CONCEPTOS > CÓDIGO) al demostrar la Inversión de Dependencias y la separación de responsabilidades. Las capas son:
1. **Dominio (Domain)**: Modelos de entidades puros en Python (`Transaction`). No hay dependencias externas aquí.
2. **Aplicación (Use Cases)**: Reglas de negocio e interfaces (`TransactionRepository` interface).
3. **Infraestructura (Infrastructure)**: Implementaciones concretas de problemas externos (`JSONTransactionRepository`).
4. **Presentación (Presentation)**: La interfaz de usuario (`CLIController`).

## Decisiones de Arquitectura

### Decisión: Usar Solo la Librería Estándar de Python

**Elección**: Usar solo módulos integrados (`json`, `datetime`, `uuid`).
**Alternativas consideradas**: Usar `pydantic` para validación de datos, `typer` para enrutamiento CLI, `pandas` para agregación de fechas.
**Justificación**: Antes de depender de librerías externas para resolver problemas "mágicamente", el desarrollador debe entender cómo parsear JSON manualmente, validar inputs y manejar cadenas de texto de fechas. Esto maximiza el aprendizaje.

### Decisión: Inyección de Dependencias

**Elección**: El Controlador CLI recibirá los Casos de Uso como dependencias, que a su vez recibirán la instancia del Repositorio JSON.
**Alternativas consideradas**: Escribir de forma fija (hardcodear) el `JSONTransactionRepository` dentro de los Casos de Uso o scripts CLI.
**Justificación**: El hardcoding acopla fuertemente la aplicación al archivo JSON. Inyectar el repositorio nos permite cambiar fácilmente el repositorio JSON por un repositorio SQLite en futuras iteraciones sin cambiar los Casos de Uso.

## Flujo de Datos

    Controlador CLI (Presentación)
          │
          ▼ (Datos de entrada: monto, categoría, tipo)
    Caso de Uso Agregar Transacción (Aplicación)
          │
          ▼ (Crea la Entidad)
    Entidad Transacción (Dominio)
          │
          ▼ (Pasa la Entidad a la Interfaz)
    Interfaz de Repositorio de Transacciones (Aplicación)
          │
          ▼ (Implementa la Interfaz)
    Repositorio JSON de Transacciones (Infraestructura)
          │
          ▼
    data/transactions.json

## Cambios en Archivos

| Archivo | Acción | Descripción |
|---------|--------|-------------|
| `src/domain/transaction.py` | Crear | Model/dataclass de Transacción. |
| `src/application/repositories.py` | Crear | Clase Base Abstracta (ABC) para la interfaz del repositorio. |
| `src/application/use_cases.py` | Crear | Contiene la lógica para Agregar, Listar y Calcular Balance. |
| `src/infrastructure/json_repository.py` | Crear | Implementación concreta para lectura/escritura de JSON. |
| `src/presentation/cli.py` | Crear | Bucle principal con `input()` y comandos `print`. |
| `main.py` | Crear | Punto de entrada de la aplicación (Configuración de Inyección de Dependencias). |
| `data/transactions.json` | Crear | Array vacío inicialmente `[]` para almacenamiento de datos. |

## Interfaces / Contratos

```python
from abc import ABC, abstractmethod
from typing import List
from domain.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Transaction]:
        pass
```

## Estrategia de Testing

| Capa | Qué Testear | Enfoque |
|------|-------------|---------|
| Unitaria | Entidad de Dominio | Asegurar que el formateo e inicialización sean correctos. |
| Unitaria | Casos de Uso | Burlar (Mockear) el `TransactionRepository` para testear el aislamiento de la lógica. |
| Integración | Repositorio JSON | Testear la lectura/escritura real del archivo usando un JSON temporal (`tempfile`). |
| E2E | Flujo de la App | Testing manual vía consola para la iteración inicial. |

## Migración / Despliegue

No se requiere migración. Proyecto nuevo (Greenfield).

## Librerías Requeridas
- `datetime` (para fechas internas)
- `json` (para persistencia)
- `uuid` (para IDs únicos)

## Preguntas Abiertas

- Ninguna. Todas las decisiones importantes resueltas. (Manejo de datos: Usaremos objetos `datetime` internamente, y los convertiremos a cadenas de texto (strings) ISO 8601 únicamente al momento de escribir en el JSON).
