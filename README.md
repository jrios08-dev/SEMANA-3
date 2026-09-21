# Quantum Core - Sistema de Transacciones

Proyecto integrador del modulo **Fundamentos de Software** (122618),
Ingenieria de Sistemas, CEIPA.
Docente: Simon Pelaez Loaiza.

## Autores

- Juana Rios

## Descripcion

Sistema que procesa transacciones financieras (credito, debito y copago).
A lo largo de las semanas 3 a 5 se aplicaron:

- **POO:** encapsulamiento, herencia y polimorfismo.
- **Principios SOLID:** analisis de SRP y OCP.
- **Confiabilidad:** manejo de excepciones con `try-except`.
- **Interoperabilidad:** serializacion y deserializacion con JSON.
- **DevOps:** control de versiones con Git y publicacion en GitHub.

## Estructura del repositorio

| Ruta | Contenido |
|------|-----------|
| `transaccion_poo_v1.py` | Semana 3 - Actividad 1: pilares de POO |
| `transacciones.txt` | Datos de prueba (formato `ID,TIPO,MONTO`) |
| `semana4/robustez_try_except.py` | Semana 4 - Actividad 1: recuperacion con try-except |
| `semana4/serializacion_json.py` | Semana 4 - Actividad 2: serializacion JSON |
| `semana4/transacciones_corruptas.txt` | Datos de prueba con errores a proposito |
| `docs/Informe_Integrador_Quantum_Core.docx` | Informe en formato APA (incluye el analisis SOLID y la configuracion de Git) |

## Como ejecutar

Requiere Python 3.

```bash
# Semana 3
python transaccion_poo_v1.py

# Semana 4 (desde la carpeta semana4)
cd semana4
python robustez_try_except.py
python serializacion_json.py
```
