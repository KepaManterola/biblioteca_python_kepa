import os
from datetime import datetime

from modelo.libro import Libro
from modelo.socio import Socio
from errores.excepciones import AlmacenamientoError

CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datos")


class GestorAlmacenamiento:

    def __init__(self, carpeta=CARPETA_DATOS):
        self.carpeta = carpeta
        self.ruta_libros = os.path.join(carpeta, "libros.txt")
        self.ruta_socios = os.path.join(carpeta, "socios.txt")
        self.ruta_log = os.path.join(carpeta, "log.txt")

    def cargar_libros(self):
        libros = []
        try:
            with open(self.ruta_libros, "r", encoding="utf-8") as fichero:
                for linea in fichero:
                    datos = linea.strip().split(";")
                    if len(datos) == 6:
                        id_socio = datos[5] if datos[5] != "" else None
                        libros.append(Libro(datos[0], datos[1], datos[2], int(datos[3]), datos[4], id_socio))
        except FileNotFoundError:
            return []
        except (OSError, ValueError) as error:
            raise AlmacenamientoError(f"No se pudo leer {self.ruta_libros}: {error}")
        return libros

    def cargar_socios(self):
        socios = []
        try:
            with open(self.ruta_socios, "r", encoding="utf-8") as fichero:
                for linea in fichero:
                    datos = linea.strip().split(";")
                    if len(datos) == 4:
                        id_libro = datos[3] if datos[3] != "" else None
                        socios.append(Socio(datos[0], datos[1], datos[2], id_libro))
        except FileNotFoundError:
            return []
        except OSError as error:
            raise AlmacenamientoError(f"No se pudo leer {self.ruta_socios}: {error}")
        return socios

    def guardar(self, libros, socios):
        try:
            os.makedirs(self.carpeta, exist_ok=True)

            with open(self.ruta_libros, "w", encoding="utf-8") as fichero:
                for libro in libros:
                    id_socio = libro.id_socio if libro.id_socio else ""
                    fichero.write(f"{libro.id_libro};{libro.titulo};{libro.autor};{libro.anio};{libro.genero};{id_socio}\n")

            with open(self.ruta_socios, "w", encoding="utf-8") as fichero:
                for socio in socios:
                    id_libro = socio.id_libro if socio.id_libro else ""
                    fichero.write(f"{socio.id_socio};{socio.nombre};{socio.email};{id_libro}\n")
        except OSError as error:
            raise AlmacenamientoError(f"No se pudieron guardar los datos: {error}")

    def escribir_log(self, evento, detalles):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try:
            with open(self.ruta_log, "a", encoding="utf-8") as fichero:
                fichero.write(f"[{fecha}][{evento}][{detalles}]\n")
        except OSError as error:
            raise AlmacenamientoError(f"No se pudo escribir el log: {error}")