from django.db import models

from apps.core.models import BaseModel
from .instrumento import Instrumento
from .dividendo import Dividendo


class EstadoCalificacion(models.TextChoices):
    ACTIVO = "ACTIVO", "Activo"
    INACTIVO = "INACTIVO", "Inactivo"


class CalificacionTributaria(BaseModel):

    instrumento = models.ForeignKey(
        Instrumento,
        on_delete=models.PROTECT,
        related_name="calificaciones",
        verbose_name="Instrumento",
    )

    dividendo = models.ForeignKey(
        Dividendo,
        on_delete=models.PROTECT,
        related_name="calificaciones",
        null=True,
        blank=True,
    )

    ejercicio = models.PositiveIntegerField(
        verbose_name="Ejercicio"
    )

    numero_evento = models.PositiveIntegerField(
        verbose_name="Número de Evento"
    )

    descripcion = models.CharField(
        max_length=255,
        verbose_name="Descripción"
    )

    isfut = models.BooleanField(
        default=False,
        verbose_name="¿Es ISFUT?"
    )

    factor_actualizacion = models.DecimalField(
        max_digits=12,
        decimal_places=8,
        verbose_name="Factor de Actualización"
    )

    estado = models.CharField(
        max_length=10,
        choices=EstadoCalificacion.choices,
        default=EstadoCalificacion.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = "calificaciones_tributarias"
        verbose_name = "Calificación Tributaria"
        verbose_name_plural = "Calificaciones Tributarias"
        ordering = ["-ejercicio", "numero_evento"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "instrumento",
                    "ejercicio",
                    "numero_evento",
                ],
                name="uq_calificacion_instrumento_ejercicio_evento",
            ),
        ]

    def __str__(self):
        return (
            f"{self.instrumento.ticker} - "
            f"{self.ejercicio} - "
            f"Evento {self.numero_evento}"
        )