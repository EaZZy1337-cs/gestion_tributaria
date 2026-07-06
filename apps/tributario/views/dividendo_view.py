from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.tributario.models import Dividendo
from apps.tributario.serializers import DividendoSerializer
from apps.tributario.services import DividendoService


class DividendoViewSet(viewsets.ModelViewSet):

    queryset = Dividendo.objects.all()
    serializer_class = DividendoSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dividendo = DividendoService.crear(
            serializer.validated_data
        )

        return Response(
            DividendoSerializer(dividendo).data,
            status=status.HTTP_201_CREATED,
        )