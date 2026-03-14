# Plan de Implementación - Fase 1: Dominio e Infraestructura Base

Vamos a poner los cimientos del proyecto. Nada de código spaghetti; vamos a separar bien las capas desde el minuto uno.

## Cambios Propuestos

### 1. Dominio (Domain)
- **Archivo**: `src/domain/transaction.py`
- **Cambio**: Crear la clase `Transaction` usando `dataclasses`.
- **Razón**: Es el corazón de la aplicación. Debe ser código Python puro, sin depender de archivos ni de la consola. Usaremos `uuid` para el ID y `datetime` para la fecha.

### 2. Aplicación (Application)
- **Archivo**: `src/application/repositories.py`
- **Cambio**: Definir la interfaz `TransactionRepository` usando `abc.ABC`.
- **Razón**: Inversión de Dependencias. La lógica no debe saber que estamos usando un JSON; solo debe saber que hay "algo" que guarda y recupera transacciones.

### 3. Infraestructura (Infrastructure)
- **Archivo**: `src/infrastructure/json_repository.py`
- **Cambio**: Implementar `JSONTransactionRepository`.
- **Razón**: Acá es donde ocurre la magia de `json.dump` y `json.load`. Manejaremos la conversión de `datetime` a string ISO para el archivo.
- **Archivo**: `data/transactions.json`
- **Cambio**: Crear el archivo con un array vacío `[]`.

## Plan de Verificación

### Tests Automatizados
1. **Test del Repositorio**:
   - Crear un test en `tests/integration/test_json_repository.py`.
   - **Instrucciones**: Ejecutar `python -m unittest tests/integration/test_json_repository.py`.
   - **Qué verifica**: Que una `Transaction` guardada se recupere con los mismos datos y que el archivo JSON se cree correctamente.

### Verificación Manual
1. Revisar que los archivos se hayan creado en la estructura de carpetas correcta (`src/domain`, `src/application`, `src/infrastructure`).
2. Abrir `data/transactions.json` y verificar que sea un JSON válido tras correr el test.
