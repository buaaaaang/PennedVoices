from .views import VisualizerViewSet, MinterViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-visualizers'

router = routers.DefaultRouter()
router.register(r'visualizers', VisualizerViewSet)
router.register(r'minters', MinterViewSet)

urlpatterns = [
    path('', include(router.urls))
]