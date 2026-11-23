class PrestamoError(Exception):

    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo


class DatosInvalidosError(Exception):
    pass


class AlmacenamientoError(Exception):
    pass