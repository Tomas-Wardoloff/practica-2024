"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        session = self.Session()
        socio = session.get(Socio, id_socio)
        session.close()
        return socio

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        session = self.Session()
        socio = session.query(Socio).filter(Socio.dni == dni_socio).first()
        session.close()
        return socio
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        session = self.Session()
        socios = session.query(Socio).all()
        session.close()
        return socios

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        session = self.Session()
        try:
            session.query(Socio).delete()
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            return False
        finally:
            session.close() 

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        session = self.Session()
        session.add(socio)
        try:
            session.commit()
            return socio
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        session = self.Session()
        try:
            result = session.query(Socio).filter(Socio.id == id_socio).delete()
            session.commit()
            return result > 0
        except Exception as e:
            session.rollback()
            return False
        finally:
            session.close()

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        session = self.Session()
        existing_socio = session.get(Socio, socio.id)
        if not existing_socio:
            session.close()
            raise ValueError("Socio no encontrado")
        
        existing_socio.nombre = socio.nombre
        existing_socio.apellido = socio.apellido
        existing_socio.dni = socio.dni
        
        try:
            session.commit()
            return existing_socio
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        session = self.Session()
        count = session.query(Socio).count()
        session.close()
        return count



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN