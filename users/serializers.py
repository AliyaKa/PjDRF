from rest_framework import serializers
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import CustomUser


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


