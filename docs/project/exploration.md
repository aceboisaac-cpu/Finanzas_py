# Exploración: Gestor de Finanzas Personales (Expense Tracker)

### Estado Actual
Proyecto nuevo (Greenfield). No hay código base existente. El usuario quiere construir una aplicación de línea de comandos (CLI) usando Python y JSON para la persistencia, con el objetivo de aprender conceptos de programación.

### Áreas Afectadas
- Creación de un nuevo proyecto dentro del espacio de trabajo.

### Enfoques Posibles
1. **Script Procedural CLI** 
   - Descripción: Un script simple o un par de funciones usando bucles `input()`.
   - Pros: Rápido de escribir, simple.
   - Contras: Difícil de testear, bajo valor educativo en cuanto a arquitectura, fuertemente acoplado al JSON.
   - Esfuerzo: Bajo

2. **Clean Architecture (Recomendado)** 
   - Descripción: Separación de responsabilidades. Entidades (Transacción), Repositorios (Almacenamiento JSON), Casos de Uso (Agregar, Listar, Resumir), y Presentación (CLI).
   - Pros: Enseña principios SOLID, altamente testeable, prepara el terreno para futuras migraciones de base de datos (SQLite/Postgres).
   - Contras: Más código repetitivo (boilerplate) para una aplicación simple.
   - Esfuerzo: Medio

### Recomendación
Se recomienda fuertemente el Enfoque 2 (Clean Architecture). El objetivo principal es el aprendizaje (CONCEPTOS > CÓDIGO). Construir una aplicación estructurada enseñará patrones escalables a futuro.

### Riesgos
- La sobre-ingeniería podría confundir al usuario inicialmente. Debemos explicar cada capa claramente.
- Complejidad en el parseo de Fechas/Horas (Date/Time) al guardar en JSON.

### Listo para Propuesta
Sí. Procediendo a la propuesta.
