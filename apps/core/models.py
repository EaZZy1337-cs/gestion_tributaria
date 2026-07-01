from django.db import models


class BaseModel(models.Model):
    """
    Modelo base para todas las entidades del sistema.
    """

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        abstract = True