from django.db import models

from apps.core.models import BaseModel


class Rol(BaseModel):

    nombre = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Nombre"
    )

    descripcion = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Descripción"
    )

    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre