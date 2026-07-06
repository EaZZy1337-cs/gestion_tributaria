from django.contrib import admin
from .models import Mercado, Instrumento



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

@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):

    list_display = (
        "ticker",
        "nombre",
        "mercado",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "ticker",
        "nombre",
        "isin",
    )

    list_filter = (
        "mercado",
        "estado",
    )

    ordering = (
        "ticker",
    )