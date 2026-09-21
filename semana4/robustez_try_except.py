# robustez_try_except.py
# Semana 4 - Gestion de errores y excepciones (try/except)
#
# Ejecutar (parado dentro de la carpeta semana4):
#     python robustez_try_except.py


class Transaccion:
    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, valor):
        if int(valor) < 0:
            raise ValueError("el monto no puede ser negativo")
        self._monto = int(valor)

    def __str__(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.monto}"


def cargar_transacciones(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue
            # --- INICIO DEL BLOQUE TRY-EXCEPT ---
            try:
                partes = linea.split(",")
                transacciones.append(Transaccion(*partes))
            except ValueError as error:
                print(f"  [Linea {numero}] ValueError: {error} "
                      f"-> se ignora: {linea}")
            except TypeError:
                print(f"  [Linea {numero}] TypeError: datos "
                      f"insuficientes -> se ignora: {linea}")
            # --- FIN DEL BLOQUE TRY-EXCEPT ---
    return transacciones


def ejecutar_sistema():
    try:
        transacciones = cargar_transacciones("transacciones_corruptas.txt")
    except FileNotFoundError:
        print("No se encontro el archivo transacciones_corruptas.txt")
        return

    print(f"\nSe procesaron {len(transacciones)} transacciones validas:")
    for t in transacciones:
        print(" ", t)


if __name__ == "__main__":
    ejecutar_sistema()
