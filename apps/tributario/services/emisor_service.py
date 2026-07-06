from apps.tributario.repositories import EmisorRepository


class EmisorService:

    @staticmethod
    def listar():
        return EmisorRepository.listar()

    @staticmethod
    def obtener(pk):
        return EmisorRepository.obtener(pk)

    @staticmethod
    def crear(datos):
        return EmisorRepository.crear(**datos)

    @staticmethod
    def actualizar(instancia, datos):
        return EmisorRepository.actualizar(instancia, **datos)

    @staticmethod
    def eliminar(instancia):
        EmisorRepository.eliminar(instancia)