from django.db import models

from apps.core.models import BaseModel
from apps.tributario.models import Mercado


class EstadoInstrumento(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class Instrumento(BaseModel):

    mercado = models.ForeignKey(
        Mercado,
        on_delete=models.PROTECT,
        related_name="instrumentos",
        verbose_name="Mercado",
    )

    ticker = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Ticker",
    )

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre",
    )

    isin = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="ISIN",
    )

    estado = models.CharField(
        max_length=10,
        choices=EstadoInstrumento.choices,
        default=EstadoInstrumento.ACTIVO,
    )

    class Meta:
        db_table = "instrumentos"
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"
        ordering = ["ticker"]

    def __str__(self):
        return f"{self.ticker} - {self.nombre}"