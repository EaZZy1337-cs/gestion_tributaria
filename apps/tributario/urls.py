from rest_framework.routers import DefaultRouter
from apps.tributario.views import (
    MercadoViewSet,
    InstrumentoViewSet,
    EmisorViewSet,
)

router = DefaultRouter()

router.register(
    "mercados",
    MercadoViewSet,
    basename="mercados",
)

router.register(
    "instrumentos",
    InstrumentoViewSet,
    basename="instrumentos",
)

router.register(
    "emisores",
    EmisorViewSet,
    basename="emisores",
)

urlpatterns = router.urls