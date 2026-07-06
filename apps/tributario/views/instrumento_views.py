from rest_framework import viewsets

from apps.tributario.models import Instrumento
from apps.tributario.serializers import InstrumentoSerializer


class InstrumentoViewSet(viewsets.ModelViewSet):

    queryset = Instrumento.objects.all()

    serializer_class = InstrumentoSerializer