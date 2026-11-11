class PrestamoError(Exception):

    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo
