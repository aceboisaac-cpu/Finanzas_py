# Tareas: Gestor de Finanzas Personales (Expense Tracker)

## Fase 1: Dominio e Infraestructura Base (Foundation)

- [x] 1.1 Crear `src/domain/transaction.py` con el modelo `Transaction` (usando `dataclass` y objetos `datetime`).
- [x] 1.2 Crear `src/application/repositories.py` con la interfaz (ABC) `TransactionRepository`.
- [x] 1.3 Crear `src/infrastructure/json_repository.py` implementando `TransactionRepository` (manejo de UUID a string y datetime a ISO 8601).
- [x] 1.4 Crear el archivo inicial vacío `data/transactions.json` (`[]`).
- [x] 1.5 Escribir tests unitarios básicos para asegurar que `JSONTransactionRepository` guarda y recupera datos correctamente (usando un archivo temporal estático).

## Fase 2: Casos de Uso (Lógica de Negocio)

- [ ] 2.1 Crear `src/application/use_cases.py` e implementar clase/función para `AddTransaction`.
- [ ] 2.2 Implementar en `use_cases.py` la lógica para `ListTransactions` (ordenadas por fecha).
- [ ] 2.3 Implementar en `use_cases.py` la lógica para `CalculateBalance` (Suma de Incomes - Suma de Expenses).
- [ ] 2.4 Escribir tests unitarios para los Casos de Uso aislando el repositorio con un Mock (usar clase Fake).

## Fase 3: Presentación (CLI) e Inyección de Dependencias

- [ ] 3.1 Crear `src/presentation/cli.py` con un bucle `while True` nativo para capturar `input()` del usuario y mostrar menús.
- [ ] 3.2 Crear `src/main.py` como punto de entrada. Aquí se instancia `JSONTransactionRepository`, se le pasa a los Use Cases, y estos al CLI.
- [ ] 3.3 Integrar menú "Agregar Transacción" (validando inputs para asegurar que el monto es numérico y la fecha tiene formato válido).
- [ ] 3.4 Integrar menú "Listar Transacciones" (mostrando datos en forma tabular).
- [ ] 3.5 Integrar menú "Ver Balance".
- [ ] 3.6 Probar integración manual de la aplicación completa tipeando comandos.

## Fase 4: Documentación y Pulido

- [ ] 4.1 Crear la carpeta `docs/learning/` (marcada en el .gitignore) para conclusiones personales en español.
- [ ] 4.2 Llenar `README.md` (Inglés) y `README.es.md` (Español) con instrucciones sobre cómo ejecutar la aplicación principal y los tests con `python -m unittest`.
