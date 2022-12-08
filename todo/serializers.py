from rest_framework import serializers
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import Projects, ToDo


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    class Meta:
        model = Projects
        fields = ['id', 'title', 'users']


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    class Meta:
        model = ToDo
        fields = ['id', 'body', 'created', 'updated', 'is_complete', 'user', 'proj']
