from rest_framework import serializers
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from users.serializers import UserModelSerializer
from .models import Projects, ToDo


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
