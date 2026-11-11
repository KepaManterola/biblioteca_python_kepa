class Socio:

    def __init__(self, id_socio, nombre, email, id_libro=None):
        self.id_socio = id_socio
        self.nombre = nombre
        self.email = email
        self.id_libro = id_libro

    def mostrar_info(self):
        print("ID:", self.id_socio)
        print("Nombre:", self.nombre)
        print("Email:", self.email)
        print("Libro prestado:", self.id_libro)

    def tiene_libro(self):
        return self.id_libro is not None