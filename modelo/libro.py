class Libro:

    def __init__(self, id_libro, titulo, autor, genero, disponible=True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible

    def mostrar_info(self):
        print("ID:", self.id_libro)
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Genero:", self.genero)
        print("Disponible:", self.disponible)
