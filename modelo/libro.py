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