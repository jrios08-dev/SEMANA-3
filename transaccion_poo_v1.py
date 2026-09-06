# ==========================================
# SEMANA 3 - PILARES DE POO Y SOLID
# ==========================================

# 1. CLASE BASE - ENCAPSULAMIENTO

class TransaccionBase:

    # Constructor
    def __init__(self, id, tipo, monto):
        self._id = id
        self._tipo = tipo
        self._monto = int(monto)

    # Getter y Setter de ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    # Getter y Setter de TIPO
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    # Getter y Setter de MONTO
    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if nuevo_monto < 0:
            raise ValueError("El monto no puede ser negativo.")

        self._monto = nuevo_monto

    # Método para obtener información
    def obtener_informacion(self):
        return f"ID: {self.id}, Tipo: {self.tipo}, Monto: {self.monto}"

    # Método para aplicar polimorfismo
    def calcular_impacto(self):
        raise NotImplementedError(
            "Este método debe ser implementado por las clases hijas."
        )


# 2. CLASE HIJA - TRANSACCIÓN CRÉDITO

class TransaccionCredito(TransaccionBase):

    def calcular_impacto(self):
        return self.monto * 0.05


# 3. CLASE HIJA - TRANSACCIÓN DÉBITO

class TransaccionDebito(TransaccionBase):

    def calcular_impacto(self):
        return 1000


# 4. LEER EL ARCHIVO Y CREAR OBJETOS

def leer_y_almacenar_datos(nombre_archivo):

    lista_transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            partes = linea.strip().split(",")

            id_transaccion = partes[0]
            tipo = partes[1]
            monto = int(partes[2])

            if tipo == "CREDITO":

                transaccion = TransaccionCredito(
                    id_transaccion,
                    tipo,
                    monto
                )

            else:

                transaccion = TransaccionDebito(
                    id_transaccion,
                    tipo,
                    monto
                )

            lista_transacciones.append(transaccion)

    return lista_transacciones


# 5. CALCULAR EL VALOR TOTAL

def calcular_valor_total(lista_transacciones):

    total = 0

    for transaccion in lista_transacciones:
        total = total + transaccion.monto

    return total


# 6. FILTRAR LAS TRANSACCIONES POR TIPO

def filtrar_por_categoria(lista_transacciones, categoria):

    lista_filtrada = []

    for transaccion in lista_transacciones:

        if transaccion.tipo == categoria:
            lista_filtrada.append(transaccion)

    return lista_filtrada


# 7. FUNCIÓN PRINCIPAL

def ejecutar_sistema():

    transacciones = leer_y_almacenar_datos("transacciones.txt")

    total = calcular_valor_total(transacciones)

    print("Valor total de las transacciones:", total)

    copagos = filtrar_por_categoria(
        transacciones,
        "COPAGO"
    )

    print("\nTransacciones de COPAGO:")

    for transaccion in copagos:
        print(transaccion.obtener_informacion())

    print("\nImpacto de las transacciones:")

    for transaccion in transacciones:

        print(
            f"ID: {transaccion.id}, "
            f"Tipo: {transaccion.tipo}, "
            f"Monto: {transaccion.monto}, "
            f"Impacto: {transaccion.calcular_impacto()}"
        )


# 8. EJECUTAR EL PROGRAMA

ejecutar_sistema()


