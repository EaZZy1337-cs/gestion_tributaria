from apps.tributario.models import Dividendo


class DividendoRepository:

    @staticmethod
    def listar():
        return Dividendo.objects.all()

    @staticmethod
    def obtener(pk):
        return Dividendo.objects.get(pk=pk)

    @staticmethod
    def crear(**datos):
        return Dividendo.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, **datos):
        for campo, valor in datos.items():
            setattr(instancia, campo, valor)

        instancia.save()
        return instancia

    @staticmethod
    def eliminar(instancia):
        instancia.delete()