from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
urlpatterns = router.urls


