from django.db import models

from apps.core.models import BaseModel


class EstadoMercado(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class Mercado(BaseModel):

    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código"
    )

    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre"
    )

    estado = models.CharField(
        max_length=10,
        choices=EstadoMercado.choices,
        default=EstadoMercado.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = "mercados"
        verbose_name = "Mercado"
        verbose_name_plural = "Mercados"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"