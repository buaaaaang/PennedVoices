from ..models import Visualizer, Minter
from rest_framework import serializers

class VisualizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualizer
        fields = '__all__'

class MinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minter
        fields = '__all__'