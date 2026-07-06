from rest_framework import serializers

from apps.tributario.models import Mercado


class MercadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mercado
        fields = (
            "id",
            "codigo",
            "nombre",
            "estado",
            "fecha_creacion",
            "fecha_actualizacion",
        )
        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_actualizacion",
        )

    def validate_codigo(self, value):
        return value.strip().upper()

    def validate_nombre(self, value):
        return value.strip()