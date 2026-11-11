from datetime import datetime

from modelo.libro import Libro
from modelo.socio import Socio
from errores.excepciones import PrestamoError

libros = []
socios = []


def cargar_datos():
    with open("libros.txt", "r", encoding="utf-8") as fichero:
        for linea in fichero:
            datos = linea.strip().split(";")
            if len(datos) == 6:
                id_socio = datos[5] if datos[5] != "" else None
                libros.append(Libro(datos[0], datos[1], datos[2], int(datos[3]), datos[4], id_socio))

    with open("socios.txt", "r", encoding="utf-8") as fichero:
        for linea in fichero:
            datos = linea.strip().split(";")
            if len(datos) == 4:
                id_libro = datos[3] if datos[3] != "" else None
                socios.append(Socio(datos[0], datos[1], datos[2], id_libro))

    print("Se ha cargado la informacion de", len(libros), "libros y", len(socios), "socios")


def guardar_datos():
    with open("libros.txt", "w", encoding="utf-8") as fichero:
        for libro in libros:
            id_socio = libro.id_socio if libro.id_socio else ""
            fichero.write(f"{libro.id_libro};{libro.titulo};{libro.autor};{libro.anio};{libro.genero};{id_socio}\n")

    with open("socios.txt", "w", encoding="utf-8") as fichero:
        for socio in socios:
            id_libro = socio.id_libro if socio.id_libro else ""
            fichero.write(f"{socio.id_socio};{socio.nombre};{socio.email};{id_libro}\n")


def escribir_log(evento, detalles):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as fichero:
        fichero.write(f"[{fecha}][{evento}][{detalles}]\n")


def buscar_libro(id_libro):
    for libro in libros:
        if libro.id_libro == id_libro:
            return libro
    return None


def buscar_socio(id_socio):
    for socio in socios:
        if socio.id_socio == id_socio:
            return socio
    return None


def mostrar_cabecera():
    print("-" * 100)
    print(f"{'ID':<6}{'TITULO':<42}{'AUTOR':<27}{'AÑO':<6}ESTADO")
    print("-" * 100)


def mostrar_libros():
    mostrar_cabecera()
    for libro in libros:
        libro.mostrar_info()


def mostrar_disponibles():
    mostrar_cabecera()
    for libro in libros:
        if libro.esta_disponible():
            libro.mostrar_info()


def buscar_por_titulo():
    termino = input("Introduce una palabra del titulo: ").lower()
    encontrados = []
    for libro in libros:
        if termino in libro.titulo.lower():
            encontrados.append(libro)

    if len(encontrados) == 0:
        print("No existe ningun libro con ese titulo")
    else:
        mostrar_cabecera()
        for libro in encontrados:
            libro.mostrar_info()


def prestar_libro():
    id_libro = input("Codigo del libro: ").upper()
    id_socio = input("Codigo del socio: ").upper()
    try:
        libro = buscar_libro(id_libro)
        socio = buscar_socio(id_socio)
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
        print("Libro", libro.titulo, "prestado a", socio.nombre)
        escribir_log("PRESTAMO", f"{libro.id_libro} {libro.titulo} -> {socio.id_socio} {socio.nombre}")
    except PrestamoError as error:
        print("Error:", error, error.codigo)


def devolver_libro():
    id_socio = input("Codigo del socio: ").upper()
    socio = buscar_socio(id_socio)
    if socio is None:
        print("No existe el socio")
    elif not socio.tiene_libro():
        print("Ese socio no tiene ningun libro")
    else:
        libro = buscar_libro(socio.id_libro)
        libro.devolver()
        socio.devolver_libro()
        print(socio.nombre, "ha devuelto", libro.titulo)
        escribir_log("DEVOLUCION", f"{socio.id_socio} {socio.nombre} devuelve {libro.id_libro} {libro.titulo}")


def mostrar_socios_con_libro():
    hay_alguno = False
    for socio in socios:
        if socio.tiene_libro():
            libro = buscar_libro(socio.id_libro)
            print(f"{socio.id_socio:<6}{socio.nombre:<25}{libro.id_libro:<6}{libro.titulo}")
            hay_alguno = True
    if not hay_alguno:
        print("Ningun socio tiene libros prestados")


def anadir_socio():
    nombre = input("Nombre: ")
    email = input("Email: ")
    id_socio = "S" + str(len(socios) + 1).zfill(3)
    socios.append(Socio(id_socio, nombre, email))
    print("Socio añadido con el codigo", id_socio)
    escribir_log("NUEVO SOCIO", f"{id_socio} {nombre}")


def anadir_libro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    try:
        anio = int(input("Año: "))
    except ValueError:
        print("El año tiene que ser un numero")
        return
    genero = input("Genero: ")
    id_libro = "L" + str(len(libros) + 1).zfill(3)
    libros.append(Libro(id_libro, titulo, autor, anio, genero))
    print("Libro añadido con el codigo", id_libro)
    escribir_log("NUEVO LIBRO", f"{id_libro} {titulo}")


def anadir():
    print("1. Añadir socio")
    print("2. Añadir libro")
    opcion = input("Elige: ")
    if opcion == "1":
        anadir_socio()
    elif opcion == "2":
        anadir_libro()
    else:
        print("Opcion no valida")


def mostrar_menu():
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


def main():
    cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            mostrar_disponibles()
        elif opcion == "3":
            buscar_por_titulo()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            mostrar_socios_con_libro()
        elif opcion == "7":
            anadir()
        elif opcion == "8":
            guardar_datos()
            print("Datos guardados")
            break
        else:
            print("Opcion no valida")


main()
