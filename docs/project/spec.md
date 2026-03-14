# Especificación del Gestor de Finanzas Personales (Expense Tracker)

## Propósito

Esta especificación define el comportamiento de la aplicación CLI "Expense Tracker". El sistema permite a los usuarios registrar, listar y resumir sus transacciones financieras personales (ingresos y gastos) utilizando un mecanismo de almacenamiento basado en JSON.

## Requerimientos

### Requerimiento: Registrar una Transacción

El sistema DEBE permitir al usuario introducir una nueva transacción con un monto, fecha, categoría y tipo (ingreso o gasto) obligatorios.

#### Escenario: Agregar un gasto con éxito
- DADO QUE la CLI está en ejecución en modo interactivo
- CUANDO el usuario selecciona "Agregar Transacción"
- Y provee monto = 50.0, fecha = "2026-03-14", categoría = "Comida", tipo = "Gasto"
- ENTONCES el sistema DEBE guardar la transacción
- Y mostrar un mensaje de éxito confirmando la adición

#### Escenario: Agregar una transacción con un monto inválido
- DADO QUE la CLI está en ejecución en modo interactivo
- CUANDO el usuario selecciona "Agregar Transacción"
- Y provee un monto no numérico (ej. "abc")
- ENTONCES el sistema DEBE rechazar la entrada
- Y mostrar un mensaje de error pidiendo un número válido

### Requerimiento: Listar Transacciones

El sistema DEBE permitir al usuario visualizar todas las transacciones registradas, ordenadas cronológically.

#### Escenario: Visualizar todas las transacciones
- DADO QUE existen transacciones en el repositorio
- CUANDO el usuario selecciona "Listar Transacciones"
- ENTONCES el sistema DEBE mostrar una tabla formateada de todas las transacciones
- Y debe incluir el conteo total de registros mostrados

#### Escenario: Visualizar transacciones cuando el repositorio está vacío
- DADO QUE no existen transacciones en el repositorio
- CUANDO el usuario selecciona "Listar Transacciones"
- ENTONCES el sistema DEBE mostrar un mensaje indicando que no se encontraron registros

### Requerimiento: Calcular el Balance

El sistema DEBE calcular y mostrar el balance financiero actual (Total Ingresos - Total Gastos).

#### Escenario: Calculando balance positivo
- DADO QUE el repositorio contiene $1000 en ingresos y $300 en gastos
- CUANDO el usuario selecciona "Mostrar Balance"
- ENTONCES el sistema DEBE calcular que el balance es de $700
- Y mostrar el total de ingresos, total de gastos y el balance neto

### Requerimiento: Almacenamiento Persistente

El sistema DEBE persistir todos los datos en un archivo JSON (`data/transactions.json`) de forma inmediata tras la creación de un nuevo registro.

#### Escenario: Persistencia estándar
- DADO QUE se ha creado una transacción válida en memoria
- CUANDO se invoca la operación de guardado del repositorio
- ENTONCES el archivo `transactions.json` DEBE ser actualizado con el nuevo registro en formato JSON estándar
