"""Base de Datos SQL - Baja"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo
    borro o no."""
    conn = sqlite3.connect("tutorial.db")
    cursor = conn.cursor()

    # Ejecuta la operación de borrado
    cursor.execute("DELETE FROM Persona WHERE IdPersona = ?", (id_persona,))

    # Verifica si alguna fila fue afectada
    filas_afectadas = cursor.rowcount
    conn.commit()
    conn.close()

    # Si se afectó al menos una fila, significa que se borró
    return filas_afectadas > 0


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert not borrar_persona(12345)


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN