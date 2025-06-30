# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        Delega la búsqueda a la capa de datos.
        :rtype: Socio
        """
        # Simplemente delegamos la llamada a la capa de datos.
        socio = self.datos.buscar(id_socio)
        return socio

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        Delega la búsqueda a la capa de datos.
        :rtype: Socio
        """
        # Delegamos la llamada a la capa de datos.
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        Delega la consulta a la capa de datos.
        :rtype: list
        """
        # Delegamos la llamada a la capa de datos.
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        # 1. Validar reglas de negocio. Si alguna falla, lanzará una excepción.
        self.regla_1(socio)
        self.regla_2(socio)
        self.regla_3()

        # 2. Si todas las validaciones pasan, delegar el alta a la capa de datos.
        self.datos.alta(socio)
        
        # 3. Devolver True indicando que la operación fue exitosa.
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        # Delegamos directamente la baja a la capa de datos.
        # La capa de datos se encargará de manejar si el ID no existe.
        self.datos.baja(id_socio)
        return True

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        # 1. Validar las reglas de negocio.
        # La consigna pide validar la regla 2.
        self.regla_2(socio)
        # Es crucial validar también la regla 1 para evitar que al modificar
        # se asigne un DNI que ya pertenece a otro socio.
        self.regla_1(socio)

        # 2. Si las validaciones pasan, delegar la modificación a la capa de datos.
        self.datos.modificacion(socio)

        # 3. Devolver True indicando éxito.
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        socio_existente = self.buscar_dni(socio.dni)
        # Si se encontró un socio con ese DNI y NO es el mismo socio que estamos validando
        # (importante para el caso de la modificación), entonces el DNI está repetido.
        if socio_existente and socio_existente.id != socio.id:
            raise DniRepetido(f"El DNI {socio.dni} ya está registrado para otro socio.")
        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        nombre_valido = self.MIN_CARACTERES <= len(socio.nombre) <= self.MAX_CARACTERES
        apellido_valido = self.MIN_CARACTERES <= len(socio.apellido) <= self.MAX_CARACTERES

        if not (nombre_valido and apellido_valido):
            raise LongitudInvalida("El nombre y el apellido deben tener entre 3 y 15 caracteres.")
        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        # Comparamos la cantidad actual de socios con el máximo permitido.
        if len(self.todos()) >= self.MAX_SOCIOS:
            raise MaximoAlcanzado(f"Se ha alcanzado el límite de {self.MAX_SOCIOS} socios.")
        return True