# serializacion_json.py
# Semana 4 - Serializacion y persistencia (JSON)
#
# Ciclo completo:
#   Serializacion:    Objeto -> Diccionario -> Cadena JSON
#   Deserializacion:  Cadena JSON -> Diccionario -> Objeto
#
# Ejecutar (parado dentro de la carpeta semana4):
#     python serializacion_json.py

import json


# --- Clases de la Semana 3 (version reducida para que este archivo
#     se pueda ejecutar solo; ver transaccion_poo_v1.py) ---
class TransaccionBase:
    def __init__(self, id, tipo, monto):
        self._id = id
        self._tipo = tipo
        self._monto = int(monto)

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo

    @property
    def monto(self):
        return self._monto


class TransaccionCredito(TransaccionBase):
    def calcular_impacto(self):
        return self.monto * 0.05


# --- 1. SERIALIZACION ---
transaccion = TransaccionCredito("T001", "CREDITO", 500000)

datos = {
    "id": transaccion.id,
    "tipo": transaccion.tipo,
    "monto": transaccion.monto,
}

cadena_json = json.dumps(datos)
print("Cadena JSON:", cadena_json)

# --- 2. DESERIALIZACION ---
datos_recuperados = json.loads(cadena_json)

# Opcion 1: argumentos posicionales
nueva_transaccion = TransaccionCredito(
    datos_recuperados["id"],
    datos_recuperados["tipo"],
    datos_recuperados["monto"],
)

# Opcion 2: argumentos nombrados (las claves coinciden con los parametros)
otra_transaccion = TransaccionCredito(**datos_recuperados)

print("Objeto reconstruido:", nueva_transaccion.id,
      nueva_transaccion.tipo, nueva_transaccion.monto)
print("Con argumentos nombrados:", otra_transaccion.id,
      otra_transaccion.tipo, otra_transaccion.monto)

# --- 3. PERSISTENCIA EN ARCHIVO ---
with open("transaccion.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)

with open("transaccion.json", "r", encoding="utf-8") as f:
    datos_leidos = json.load(f)

print("Leido desde archivo:", datos_leidos)
