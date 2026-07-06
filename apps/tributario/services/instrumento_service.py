from apps.tributario.repositories import InstrumentoRepository


class InstrumentoService:

    @staticmethod
    def listar():
        return InstrumentoRepository.listar()

    @staticmethod
    def obtener(pk):
        return InstrumentoRepository.obtener(pk)

    @staticmethod
    def crear(datos):
        return InstrumentoRepository.crear(**datos)

    @staticmethod
    def actualizar(instancia, datos):
        return InstrumentoRepository.actualizar(instancia, **datos)

    @staticmethod
    def eliminar(instancia):
        InstrumentoRepository.eliminar(instancia)