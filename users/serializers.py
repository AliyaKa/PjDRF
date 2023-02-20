from rest_framework import serializers
from .models import CustomUser


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'firstname', 'lastname', 'email']


