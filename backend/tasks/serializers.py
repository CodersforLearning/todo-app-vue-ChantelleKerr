from django.db.models.base import Model
from .models import Task
from rest_framework.serializers import ModelField, ModelSerializer

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'