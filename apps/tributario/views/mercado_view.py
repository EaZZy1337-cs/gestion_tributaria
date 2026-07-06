from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from apps.tributario.models import Mercado
from apps.tributario.serializers import MercadoSerializer
from apps.tributario.services import MercadoService


class MercadoViewSet(viewsets.ModelViewSet):

    queryset = Mercado.objects.all()

    serializer_class = MercadoSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        mercado = MercadoService.crear(serializer.validated_data)

        return Response(
            MercadoSerializer(mercado).data,
            status=status.HTTP_201_CREATED,
        )