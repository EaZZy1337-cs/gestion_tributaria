from rest_framework import serializers

from apps.tributario.models import Emisor


class EmisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emisor
        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_actualizacion",
        )