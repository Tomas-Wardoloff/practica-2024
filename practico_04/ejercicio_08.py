"""Base de datos SQL - Listar"""

import datetime
import sqlite3

from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona  # Importamos la función para validar
from ejercicio_06 import reset_tabla
from ejercicio_07 import agregar_peso


def listar_pesos(id_persona):
    """Implementar la funcion listar_pesos, que devuelva el historial de pesos
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya
     implementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """

    # 1. Validar que la persona existe
    if not buscar_persona(id_persona):
        return False

    # 2. Conectar a la BD y obtener los datos
    conn = sqlite3.connect("tutorial.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Fecha, Peso FROM PersonaPeso WHERE IdPersona = ? ORDER BY Fecha",
        (id_persona,)
    )
    resultados = cursor.fetchall()
    conn.close()

    # 3. Formatear la lista de resultados al formato requerido
    # Usamos una "list comprehension" para hacerlo de forma concisa.
    lista_formateada = [
        (datetime.datetime.fromisoformat(fila[0]).strftime('%Y-%m-%d'), fila[1])
        for fila in resultados
    ]

    return lista_formateada


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN