from rest_framework import viewsets

from apps.tributario.models import Emisor
from apps.tributario.serializers import EmisorSerializer


class EmisorViewSet(viewsets.ModelViewSet):

    queryset = Emisor.objects.all()

    serializer_class = EmisorSerializer