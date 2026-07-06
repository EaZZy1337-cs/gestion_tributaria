from rest_framework.exceptions import ValidationError

from apps.tributario.models import Dividendo
from apps.tributario.repositories import DividendoRepository


class DividendoService:

    @staticmethod
    def listar():
        return DividendoRepository.listar()

    @staticmethod
    def obtener(pk):
        return DividendoRepository.obtener(pk)

    @staticmethod
    def crear(datos):

        if datos["monto"] <= 0:
            raise ValidationError(
                "El monto del dividendo debe ser mayor que cero."
            )

        if datos["fecha_pago"] < datos["fecha_corte"]:
            raise ValidationError(
                "La fecha de pago no puede ser anterior a la fecha de corte."
            )

        existe = Dividendo.objects.filter(
            instrumento=datos["instrumento"],
            fecha_pago=datos["fecha_pago"],
        ).exists()

        if existe:
            raise ValidationError(
                "Ya existe un dividendo para este instrumento en esa fecha."
            )

        return DividendoRepository.crear(**datos)

    @staticmethod
    def actualizar(instancia, datos):
        return DividendoRepository.actualizar(instancia, **datos)

    @staticmethod
    def eliminar(instancia):
        DividendoRepository.eliminar(instancia)