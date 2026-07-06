from apps.tributario.models import Mercado


class MercadoRepository:

    @staticmethod
    def listar():
        return Mercado.objects.order_by("nombre")

    @staticmethod
    def obtener(pk):
        return Mercado.objects.filter(pk=pk).first()

    @staticmethod
    def buscar_por_codigo(codigo):
        return Mercado.objects.filter(codigo=codigo).first()

    @staticmethod
    def buscar_por_nombre(nombre):
        return Mercado.objects.filter(nombre=nombre).first()

    @staticmethod
    def crear(**datos):
        return Mercado.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, **datos):
        for campo, valor in datos.items():
            setattr(instancia, campo, valor)

        instancia.save()
        return instancia

    @staticmethod
    def eliminar(instancia):
        instancia.delete()