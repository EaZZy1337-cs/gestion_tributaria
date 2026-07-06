from apps.tributario.models import Instrumento


class InstrumentoRepository:

    @staticmethod
    def listar():
        return Instrumento.objects.all()

    @staticmethod
    def obtener(pk):
        return Instrumento.objects.get(pk=pk)

    @staticmethod
    def crear(**datos):
        return Instrumento.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, **datos):
        for campo, valor in datos.items():
            setattr(instancia, campo, valor)

        instancia.save()
        return instancia

    @staticmethod
    def eliminar(instancia):
        instancia.delete()