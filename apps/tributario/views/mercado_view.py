from rest_framework import viewsets

from apps.tributario.models import Mercado
from apps.tributario.serializers import MercadoSerializer


class MercadoViewSet(viewsets.ModelViewSet):

    queryset = Mercado.objects.order_by("nombre")

    serializer_class = MercadoSerializer