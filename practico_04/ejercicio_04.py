"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla, borrar_tabla, crear_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    conn = sqlite3.connect("tutorial.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM persona WHERE IdPersona = ?", (id_persona,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        id, nombre, nacimiento_str, dni, altura = resultado
        nacimiento = datetime.datetime.strptime(nacimiento_str, "%Y-%m-%d %H:%M:%S")
        return (id, nombre, nacimiento, dni, altura)
    else:
        return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
