from apps.tributario.repositories import MercadoRepository


class MercadoService:

    @staticmethod
    def listar():
        return MercadoRepository.listar()

    @staticmethod
    def obtener(pk):
        return MercadoRepository.obtener(pk)

    @staticmethod
    def crear(datos):

        if MercadoRepository.buscar_por_codigo(datos["codigo"]):
            raise ValueError("Ya existe un mercado con ese código.")

        if MercadoRepository.buscar_por_nombre(datos["nombre"]):
            raise ValueError("Ya existe un mercado con ese nombre.")

        return MercadoRepository.crear(**datos)

    @staticmethod
    def actualizar(instancia, datos):
        return MercadoRepository.actualizar(instancia, **datos)

    @staticmethod
    def eliminar(instancia):
        MercadoRepository.eliminar(instancia)