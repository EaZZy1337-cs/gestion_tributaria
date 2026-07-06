from django.db import models

from apps.core.models import BaseModel


class EstadoEmisor(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class Emisor(BaseModel):

    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código"
    )

    nombre = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Nombre"
    )

    pais = models.CharField(
        max_length=100,
        default="Chile",
        verbose_name="País"
    )

    estado = models.CharField(
        max_length=10,
        choices=EstadoEmisor.choices,
        default=EstadoEmisor.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = "emisores"
        verbose_name = "Emisor"
        verbose_name_plural = "Emisores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre