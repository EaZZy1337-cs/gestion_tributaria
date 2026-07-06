from rest_framework import serializers

from apps.tributario.models import Dividendo


class DividendoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dividendo
        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_actualizacion",
        )