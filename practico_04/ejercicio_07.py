import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    if not buscar_persona(id_persona):
        return False

    ultima_fecha_registrada = buscar_peso(id_persona)

    if ultima_fecha_registrada and fecha <= ultima_fecha_registrada:
        return False

    conn = sqlite3.connect("tutorial.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) VALUES (?, ?, ?)",
        (id_persona, fecha, peso)
    )
    nuevo_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return nuevo_id


def buscar_peso(id_persona):
    """
    Busca la fecha del último registro de peso para una persona.
    Devuelve un objeto datetime con la fecha si lo encuentra, o None si no.
    """
    conn = sqlite3.connect("tutorial.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT Fecha FROM PersonaPeso WHERE IdPersona = ? ORDER BY Fecha DESC LIMIT 1",
        (id_persona,)
    )
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return datetime.datetime.fromisoformat(resultado[0])

    return None


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) is False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN