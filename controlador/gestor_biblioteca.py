class GestorBiblioteca:

    def __init__(self, biblioteca, almacenamiento):
        self.biblioteca = biblioteca
        self.almacenamiento = almacenamiento

    # ---------- Datos ----------

    def cargar_datos(self):
        libros = self.almacenamiento.cargar_libros()
        socios = self.almacenamiento.cargar_socios()
        self.biblioteca.cargar(libros, socios)
        return len(libros), len(socios)

    def guardar_datos(self):
        self.almacenamiento.guardar(self.biblioteca.libros, self.biblioteca.socios)

    # ---------- Consultas ----------

    def todos_los_libros(self):
        return self.biblioteca.libros

    def libros_disponibles(self):
        return self.biblioteca.libros_disponibles()

    def buscar_por_titulo(self, termino):
        return self.biblioteca.buscar_por_titulo(termino)

    def socios_con_libro(self):
        return self.biblioteca.socios_con_libro()

    # ---------- Operaciones que modifican datos ----------

    def prestar(self, id_libro, id_socio):
        libro, socio = self.biblioteca.prestar(id_libro, id_socio)
        self.almacenamiento.escribir_log("PRESTAMO", f"{libro.id_libro} {libro.titulo} -> {socio.id_socio} {socio.nombre}")
        self.guardar_datos()
        return libro, socio

    def devolver(self, id_socio):
        libro, socio = self.biblioteca.devolver(id_socio)
        self.almacenamiento.escribir_log("DEVOLUCION", f"{socio.id_socio} {socio.nombre} devuelve {libro.id_libro} {libro.titulo}")
        self.guardar_datos()
        return libro, socio

    def anadir_socio(self, nombre, email):
        socio = self.biblioteca.anadir_socio(nombre, email)
        self.almacenamiento.escribir_log("NUEVO SOCIO", f"{socio.id_socio} {socio.nombre}")
        self.guardar_datos()
        return socio

    def anadir_libro(self, titulo, autor, anio, genero):
        libro = self.biblioteca.anadir_libro(titulo, autor, anio, genero)
        self.almacenamiento.escribir_log("NUEVO LIBRO", f"{libro.id_libro} {libro.titulo}")
        self.guardar_datos()
        return libro