from rest_framework.viewsets import ModelViewSet
from .models import Projects, ToDo
from .serializers import ProjectsSerializer, ToDoSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

