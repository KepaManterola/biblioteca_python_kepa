class Libro:

    def __init__(self, id_libro, titulo, autor, anio, genero, id_socio=None):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.id_socio = id_socio

    def esta_disponible(self):
        return self.id_socio is None

    def prestar(self, id_socio):
        self.id_socio = id_socio

    def devolver(self):
        self.id_socio = None

    def mostrar_info(self):
        if self.esta_disponible():
            estado = "Disponible"
        else:
            estado = "Prestado a " + self.id_socio
        print(f"{self.id_libro:<6}{self.titulo[:40]:<42}{self.autor[:25]:<27}{self.anio:<6}{estado}")
