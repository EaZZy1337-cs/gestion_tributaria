from rest_framework import serializers

from apps.tributario.models import CalificacionTributaria


class CalificacionSerializer(serializers.ModelSerializer):
    """
    Serializer para las Calificaciones Tributarias.
    """

    class Meta:
        model = CalificacionTributaria
        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_actualizacion",
        )