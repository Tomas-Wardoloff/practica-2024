"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3


def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT(30),
            FechaNacimiento DATE,
            DNI INTEGER,
            Altura INTEGER
        )
    ''')
    con.commit()
    con.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS Persona
    ''')
    con.commit()
    con.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def wrapper():
        borrar_tabla()
        crear_tabla()
        return func()
    return wrapper
# NO MODIFICAR - FIN