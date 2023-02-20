from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import CustomUser
from .serializers import UserModelSerializer


class CustomUserViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
