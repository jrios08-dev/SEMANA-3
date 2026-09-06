# Actividad Semana 2 - Programación Orientada a Objetos

## Refactorización de transacciones de PE a POO

### 1. Análisis de fragilidad

En la Semana 1 se utilizó Programación Estructurada (PE) para leer y procesar las transacciones. Los datos de cada transacción se almacenaban en diccionarios con los campos ID, Tipo y Monto.

Además, la lógica estaba separada en diferentes funciones: una función para cargar las transacciones, otra para calcular el valor total y otra para filtrar las transacciones por categoría.

Esta separación puede generar un riesgo de debugging cuando se necesiten manejar 10 tipos de transacciones diferentes. Si los datos o su estructura cambian, sería necesario revisar y modificar diferentes funciones del programa para evitar errores.

Por ejemplo, la función que calcula el valor total necesita conocer que el monto se encuentra en el campo "Monto", mientras que la función que filtra necesita conocer que el tipo está almacenado en el campo "Tipo".

Al tener los datos separados de la lógica, aumenta el riesgo de modificar una parte del programa y afectar otra.

Por esta razón, se realizó una refactorización utilizando Programación Orientada a Objetos (POO), agrupando los datos y comportamientos relacionados dentro de una clase.

### 2. Definición de la clase Transaccion

Se creó la clase `Transaccion`, la cual representa una entidad del sistema.

La clase utiliza el constructor `__init__` para encapsular los datos de cada transacción como atributos del objeto:

- ID
- Tipo
- Monto

El constructor utilizado es:

python
def __init__(self, id, tipo, monto):
    self.id = id
    self.tipo = tipo
    self.monto = monto