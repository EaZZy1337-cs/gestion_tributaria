from django.contrib import admin

from apps.tributario.models import (
    Mercado,
    Instrumento,
    Emisor,
)


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
        "emisor",
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
        "emisor",
        "mercado",
        "estado",
    )

    ordering = (
        "ticker",
    )

@admin.register(Emisor)
class EmisorAdmin(admin.ModelAdmin):

    list_display = (
        "codigo",
        "nombre",
        "pais",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "nombre",
    )

    list_filter = (
        "pais",
        "estado",
    )

    ordering = (
        "nombre",
    )