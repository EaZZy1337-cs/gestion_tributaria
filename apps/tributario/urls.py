from rest_framework.routers import DefaultRouter

from apps.tributario.views.mercado_view import MercadoViewSet

router = DefaultRouter()

router.register(
    "mercados",
    MercadoViewSet,
    basename="mercados",
)

urlpatterns = router.urls