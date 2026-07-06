from rest_framework.routers import DefaultRouter
from apps.tributario.views import (
    MercadoViewSet,
    InstrumentoViewSet,
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

urlpatterns = router.urls