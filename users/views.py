from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserModelSerializer


class UserModelAPIView(APIView):

    def get(self, request):
        queryset = CustomUser.objects.all()
        return Response({'users': UserModelSerializer(queryset, many=True).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = CustomUser.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = UserModelSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})


