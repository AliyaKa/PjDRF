from django.http import Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Projects, ToDo
from .serializers import ProjectsSerializer, ToDoSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class ProjectsModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ToDoViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(ToDo)

    def destroy(self,request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(ToDo)

