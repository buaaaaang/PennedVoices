from rest_framework import viewsets
from .serializers import VisualizerSerializer, MinterSerializer
from ..models import Visualizer, Minter

class VisualizerViewSet(viewsets.ModelViewSet):
    queryset= Visualizer.objects.all().order_by('-uploaded')
    serializer_class = VisualizerSerializer

class MinterViewSet(viewsets.ModelViewSet):
    queryset= Minter.objects.all().order_by('-imageID')
    serializer_class = MinterSerializer