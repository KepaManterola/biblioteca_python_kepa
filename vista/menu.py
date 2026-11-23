from errores.excepciones import PrestamoError, DatosInvalidosError, AlmacenamientoError


class Menu:

    def __init__(self, gestor):
        self.gestor = gestor

    def iniciar(self):
        try:
            num_libros, num_socios = self.gestor.cargar_datos()
        except AlmacenamientoError as error:
            print("Error:", error)
            return
        print("Se ha cargado la informacion de", num_libros, "libros y", num_socios, "socios")

        while True:
            self.mostrar_opciones()
            opcion = input("Elige una opcion: ")
            if opcion == "1":
                self.mostrar_libros(self.gestor.todos_los_libros())
            elif opcion == "2":
                self.mostrar_libros(self.gestor.libros_disponibles())
            elif opcion == "3":
                self.opcion_buscar_por_titulo()
            elif opcion == "4":
                self.opcion_prestar()
            elif opcion == "5":
                self.opcion_devolver()
            elif opcion == "6":
                self.opcion_socios_con_libro()
            elif opcion == "7":
                self.opcion_anadir()
            elif opcion == "8":
                self.opcion_salir()
                break
            else:
                print("Opcion no valida")

    def mostrar_opciones(self):
        print()
        print("===== BIBLIOTECA =====")
        print("1. Mostrar todos los libros")
        print("2. Mostrar libros disponibles")
        print("3. Buscar libro por titulo")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Socios con libro")
        print("7. Añadir socios y libros")
        print("8. Salir")

    def mostrar_cabecera(self):
        print("-" * 100)
        print(f"{'ID':<6}{'TITULO':<42}{'AUTOR':<27}{'AÑO':<6}ESTADO")
        print("-" * 100)

    def mostrar_libro(self, libro):
        if libro.esta_disponible():
            estado = "Disponible"
        else:
            estado = "Prestado a " + libro.id_socio
        print(f"{libro.id_libro:<6}{libro.titulo[:40]:<42}{libro.autor[:25]:<27}{libro.anio:<6}{estado}")

    def mostrar_libros(self, libros):
        self.mostrar_cabecera()
        for libro in libros:
            self.mostrar_libro(libro)

    def opcion_buscar_por_titulo(self):
        termino = input("Introduce una palabra del titulo: ")
        encontrados = self.gestor.buscar_por_titulo(termino)
        if len(encontrados) == 0:
            print("No existe ningun libro con ese titulo")
        else:
            self.mostrar_libros(encontrados)

    def opcion_prestar(self):
        id_libro = input("Codigo del libro: ").upper()
        id_socio = input("Codigo del socio: ").upper()
        try:
            libro, socio = self.gestor.prestar(id_libro, id_socio)
            print("Libro", libro.titulo, "prestado a", socio.nombre)
        except PrestamoError as error:
            print("Error:", error, error.codigo)
        except AlmacenamientoError as error:
            print("Error:", error)

    def opcion_devolver(self):
        id_socio = input("Codigo del socio: ").upper()
        try:
            libro, socio = self.gestor.devolver(id_socio)
            print(socio.nombre, "ha devuelto", libro.titulo)
        except PrestamoError as error:
            print("Error:", error, error.codigo)
        except AlmacenamientoError as error:
            print("Error:", error)

    def opcion_socios_con_libro(self):
        lista = self.gestor.socios_con_libro()
        if len(lista) == 0:
            print("Ningun socio tiene libros prestados")
        else:
            for socio, libro in lista:
                print(f"{socio.id_socio:<6}{socio.nombre:<25}{libro.id_libro:<6}{libro.titulo}")

    def opcion_anadir(self):
        print("1. Añadir socio")
        print("2. Añadir libro")
        opcion = input("Elige: ")
        if opcion == "1":
            self.opcion_anadir_socio()
        elif opcion == "2":
            self.opcion_anadir_libro()
        else:
            print("Opcion no valida")

    def opcion_anadir_socio(self):
        nombre = input("Nombre: ")
        email = input("Email: ")
        try:
            socio = self.gestor.anadir_socio(nombre, email)
            print("Socio añadido con el codigo", socio.id_socio)
        except AlmacenamientoError as error:
            print("Error:", error)

    def opcion_anadir_libro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        anio = input("Año: ")
        genero = input("Genero: ")
        try:
            libro = self.gestor.anadir_libro(titulo, autor, anio, genero)
            print("Libro añadido con el codigo", libro.id_libro)
        except DatosInvalidosError as error:
            print("Error:", error)
        except AlmacenamientoError as error:
            print("Error:", error)

    def opcion_salir(self):
        try:
            self.gestor.guardar_datos()
            print("Datos guardados")
        except AlmacenamientoError as error:
            print("Error:", error)