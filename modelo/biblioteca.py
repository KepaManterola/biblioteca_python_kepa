from modelo.libro import Libro
from modelo.socio import Socio
from errores.excepciones import PrestamoError, DatosInvalidosError


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.socios = []

    def cargar(self, libros, socios):
        self.libros = libros
        self.socios = socios

    def buscar_libro(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        return None

    def buscar_socio(self, id_socio):
        for socio in self.socios:
            if socio.id_socio == id_socio:
                return socio
        return None

    def libros_disponibles(self):
        disponibles = []
        for libro in self.libros:
            if libro.esta_disponible():
                disponibles.append(libro)
        return disponibles

    def buscar_por_titulo(self, termino):
        termino = termino.lower()
        encontrados = []
        for libro in self.libros:
            if termino in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados

    def socios_con_libro(self):
        resultado = []
        for socio in self.socios:
            if socio.tiene_libro():
                libro = self.buscar_libro(socio.id_libro)
                resultado.append((socio, libro))
        return resultado

    def prestar(self, id_libro, id_socio):
        libro = self.buscar_libro(id_libro)
        socio = self.buscar_socio(id_socio)
        if libro is None:
            raise PrestamoError("No existe el libro", id_libro)
        if socio is None:
            raise PrestamoError("No existe el socio", id_socio)
        if socio.tiene_libro():
            raise PrestamoError("El socio ya tiene el libro", socio.id_libro)
        if not libro.esta_disponible():
            raise PrestamoError("El libro lo tiene el socio", libro.id_socio)

        libro.prestar(socio.id_socio)
        socio.coger_libro(libro.id_libro)
        return libro, socio

    def devolver(self, id_socio):
        socio = self.buscar_socio(id_socio)
        if socio is None:
            raise PrestamoError("No existe el socio", id_socio)
        if not socio.tiene_libro():
            raise PrestamoError("Ese socio no tiene ningun libro", id_socio)

        libro = self.buscar_libro(socio.id_libro)
        libro.devolver()
        socio.devolver_libro()
        return libro, socio

    def anadir_socio(self, nombre, email):
        id_socio = "S" + str(len(self.socios) + 1).zfill(3)
        socio = Socio(id_socio, nombre, email)
        self.socios.append(socio)
        return socio

    def anadir_libro(self, titulo, autor, anio, genero):
        try:
            anio = int(anio)
        except ValueError:
            raise DatosInvalidosError("El año tiene que ser un numero")

        id_libro = "L" + str(len(self.libros) + 1).zfill(3)
        libro = Libro(id_libro, titulo, autor, anio, genero)
        self.libros.append(libro)
        return libro