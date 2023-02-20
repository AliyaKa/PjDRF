from rest_framework import serializers
from .models import Projects, ToDo


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
       # exclude = ('is_complete',)
        fields = ['id', 'body', 'created', 'updated', 'user', 'proj']
