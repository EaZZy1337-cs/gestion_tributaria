from django.contrib import admin

from .models import Mercado


@admin.register(Mercado)
class MercadoAdmin(admin.ModelAdmin):

    list_display = (
        "codigo",
        "nombre",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "nombre",
    )

    list_filter = (
        "estado",
    )

    ordering = (
        "nombre",
    )