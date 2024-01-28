from rest_framework import serializers
from .models import *


class KordinatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kordinators
        fields = ('name',)
        
class TaskSerializer(serializers.ModelSerializer):
    coordinators = serializers.StringRelatedField(many=True)
    class Meta:
        model = Task
        fields = '__all__'
