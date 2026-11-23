from persistencia.gestor_almacenamiento import GestorAlmacenamiento
from modelo.biblioteca import Biblioteca
from controlador.gestor_biblioteca import GestorBiblioteca
from vista.menu import Menu


def main():
    almacenamiento = GestorAlmacenamiento()
    biblioteca = Biblioteca()
    gestor = GestorBiblioteca(biblioteca, almacenamiento)
    menu = Menu(gestor)
    menu.iniciar()


if __name__ == "__main__":
    main()