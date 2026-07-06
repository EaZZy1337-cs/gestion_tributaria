from apps.tributario.models import CalificacionTributaria


class CalificacionRepository:
    """
    Repositorio encargado de acceder a los datos de las
    Calificaciones Tributarias.
    """

    @staticmethod
    def listar():
        return CalificacionTributaria.objects.all()

    @staticmethod
    def obtener(pk):
        return CalificacionTributaria.objects.get(pk=pk)

    @staticmethod
    def crear(**datos):
        return CalificacionTributaria.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, **datos):

        for campo, valor in datos.items():
            setattr(instancia, campo, valor)

        instancia.save()

        return instancia

    @staticmethod
    def eliminar(instancia):
        instancia.delete()

    @staticmethod
    def existe(instrumento, ejercicio, numero_evento):

        return CalificacionTributaria.objects.filter(
            instrumento=instrumento,
            ejercicio=ejercicio,
            numero_evento=numero_evento,
        ).exists()