from rest_framework import serializers
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from users.serializers import UserModelSerializer
from .models import Projects, ToDo


class ProjectsSerializer(serializers.ModelSerializer):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    users = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Projects
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    user = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
