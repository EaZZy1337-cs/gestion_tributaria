from django.db import models

from apps.core.models import BaseModel
from .instrumento import Instrumento


class MonedaEnum(models.TextChoices):
    CLP = "CLP", "Peso Chileno"
    USD = "USD", "Dólar Estadounidense"
    EUR = "EUR", "Euro"


class TipoDividendoEnum(models.TextChoices):
    ORDINARIO = "ORDINARIO", "Ordinario"
    EXTRAORDINARIO = "EXTRAORDINARIO", "Extraordinario"


class EstadoDividendo(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class Dividendo(BaseModel):

    instrumento = models.ForeignKey(
        Instrumento,
        on_delete=models.PROTECT,
        related_name="dividendos",
        verbose_name="Instrumento",
    )

    fecha_corte = models.DateField(
        verbose_name="Fecha de corte",
    )

    fecha_pago = models.DateField(
        verbose_name="Fecha de pago",
    )

    monto = models.DecimalField(
        max_digits=15,
        decimal_places=4,
        verbose_name="Monto",
    )

    moneda = models.CharField(
        max_length=3,
        choices=MonedaEnum.choices,
        default=MonedaEnum.CLP,
        verbose_name="Moneda",
    )

    tipo_dividendo = models.CharField(
        max_length=20,
        choices=TipoDividendoEnum.choices,
        default=TipoDividendoEnum.ORDINARIO,
        verbose_name="Tipo de dividendo",
    )

    estado = models.CharField(
        max_length=10,
        choices=EstadoDividendo.choices,
        default=EstadoDividendo.ACTIVO,
        verbose_name="Estado",
    )

    class Meta:
        db_table = "dividendos"
        verbose_name = "Dividendo"
        verbose_name_plural = "Dividendos"
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"{self.instrumento.ticker} - {self.fecha_pago}"