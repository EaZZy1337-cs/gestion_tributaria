from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.tributario.models import CalificacionTributaria
from apps.tributario.serializers import CalificacionSerializer
from apps.tributario.services import CalificacionService


class CalificacionViewSet(viewsets.ModelViewSet):
    """
    API para administrar las Calificaciones Tributarias.
    """

    queryset = CalificacionTributaria.objects.all()

    serializer_class = CalificacionSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        calificacion = CalificacionService.registrar_calificacion(
            serializer.validated_data
        )

        return Response(
            CalificacionSerializer(calificacion).data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):

        instancia = self.get_object()

        serializer = self.get_serializer(
            instancia,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        calificacion = CalificacionService.actualizar_calificacion(
            instancia,
            serializer.validated_data,
        )

        return Response(
            CalificacionSerializer(calificacion).data
        )

    def destroy(self, request, *args, **kwargs):

        instancia = self.get_object()

        CalificacionService.eliminar(instancia)

        return Response(status=status.HTTP_204_NO_CONTENT)