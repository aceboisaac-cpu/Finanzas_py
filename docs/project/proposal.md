# Propuesta: Gestor de Finanzas Personales (Expense Tracker)

## Intención
Crear una aplicación CLI (línea de comandos) en Python para gestionar gastos e ingresos. El objetivo principal es el aprendizaje de **Clean Architecture** (Arquitectura Limpia), la persistencia de datos usando JSON, y la separación de responsabilidades.

## Alcance

### En Alcance (In Scope)
- Entidades principales: `Transaction` (id, monto, fecha, categoría, tipo: ingreso/gasto).
- Persistencia de datos en JSON (Capa de Repositorio).
- Casos de uso: Agregar Transacción, Listar Transacciones, Obtener Balance.
- Interacción mediante Interfaz de Línea de Comandos (CLI).

### Fuera de Alcance (Out of Scope)
- Interfaz web o gráfica.
- Integración con base de datos relacional (dejado para futura iteración).
- Autenticación o soporte multi-usuario.

## Enfoque
Implementar una estructura de Clean Architecture:
1. **Dominio**: Objetos Python puros (`Transaction`).
2. **Aplicación (Casos de Uso)**: Reglas de negocio (ej. calcular totales, filtrar por mes).
3. **Infraestructura**: Interacción con el sistema de archivos (módulo `json`).
4. **Presentación**: CLI usando `input()` nativo o `argparse`.

## Áreas Afectadas

| Área | Impacto | Descripción |
|------|---------|-------------|
| `src/domain/` | Nuevo | Modelos core e interfaces |
| `src/application/` | Nuevo | Casos de uso (lógica de negocio) |
| `src/infrastructure/`| Nuevo | Implementación del Repositorio JSON |
| `src/presentation/` | Nuevo | Punto de entrada del CLI |
| `data/` | Nuevo | Ubicación de almacenamiento JSON |
| `docs/project/` | Nuevo | Documentación técnica Inglés/Español |

## Riesgos

| Riesgo | Probabilidad | Mitigación |
|--------|--------------|------------|
| Corrupción de datos JSON | Baja | Implementar escritura segura. |
| Sobre-ingeniería | Media | Mantener casos de uso simples y explicar el "por qué" de cada capa. |

## Plan de Rollback
Dado que este es un proyecto completamente nuevo (greenfield), el rollback consiste en eliminar los directorios recién creados y resetear la rama de Git.

## Dependencias
- Python 3.10+
- Librerías nativas (`json`, `datetime`, `uuid`).
- Sin dependencias externas para la app principal.

## Criterios de Éxito
- [ ] El usuario puede agregar un gasto o ingreso por terminal.
- [ ] Las transacciones se guardan en `data/transactions.json` sin pérdida de datos.
- [ ] El usuario puede consultar su balance total.
- [ ] El código sigue las reglas de dependencia de Clean Architecture.
