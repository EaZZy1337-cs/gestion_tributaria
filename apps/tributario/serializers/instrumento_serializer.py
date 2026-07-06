from rest_framework import serializers

from apps.tributario.models import Instrumento


class InstrumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrumento
        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_actualizacion",
        )