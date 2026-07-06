from django.contrib import admin

from apps.tributario.models import (
    Mercado,
    Instrumento,
    Emisor,
    Dividendo,
    CalificacionTributaria,
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

@admin.register(Dividendo)
class DividendoAdmin(admin.ModelAdmin):

    list_display = (
        "instrumento",
        "fecha_corte",
        "fecha_pago",
        "monto",
        "moneda",
        "tipo_dividendo",
        "estado",
    )

    list_filter = (
        "moneda",
        "tipo_dividendo",
        "estado",
    )

    ordering = (
        "-fecha_pago",
    )

@admin.register(CalificacionTributaria)
class CalificacionTributariaAdmin(admin.ModelAdmin):

    list_display = (
        "instrumento",
        "ejercicio",
        "numero_evento",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "instrumento__ticker",
        "descripcion",
    )

    list_filter = (
        "ejercicio",
        "estado",
    )

    ordering = (
        "-ejercicio",
        "numero_evento",
    )