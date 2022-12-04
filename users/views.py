from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import CustomUser
from .serializers import UserModelSerializer


class UserModelCustomViewSet(mixins.ListModelMixin,
                             mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
