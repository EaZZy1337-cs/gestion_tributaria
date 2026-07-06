from apps.tributario.models import Emisor


class EmisorRepository:

    @staticmethod
    def listar():
        return Emisor.objects.all()

    @staticmethod
    def obtener(pk):
        return Emisor.objects.get(pk=pk)

    @staticmethod
    def crear(**datos):
        return Emisor.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, **datos):
        for campo, valor in datos.items():
            setattr(instancia, campo, valor)

        instancia.save()
        return instancia

    @staticmethod
    def eliminar(instancia):
        instancia.delete()