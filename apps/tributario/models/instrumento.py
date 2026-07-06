from django.db import models
from .emisor import Emisor
from apps.core.models import BaseModel
from .mercado import Mercado


class EstadoInstrumento(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class Instrumento(BaseModel):

    ticker = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Ticker"
    )

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre"
    )

    isin = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="ISIN"
    )

    mercado = models.ForeignKey(
        Mercado,
        on_delete=models.PROTECT,
        related_name="instrumentos",
        verbose_name="Mercado"
    )

    emisor = models.ForeignKey(
        Emisor,
        on_delete=models.PROTECT,
        related_name="instrumentos",
        verbose_name="Emisor",
    )
    
    estado = models.CharField(
        max_length=10,
        choices=EstadoInstrumento.choices,
        default=EstadoInstrumento.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = "instrumentos"
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"
        ordering = ["ticker"]

    def __str__(self):
        return f"{self.ticker} - {self.nombre}"