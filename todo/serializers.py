from rest_framework import serializers
from .models import Projects, ToDo


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'
