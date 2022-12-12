from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Projects, ToDo
from .serializers import ProjectsSerializer, ToDoSerializer


# class ProjectsAPIListPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


class ProjectsModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    #pagination_class = ProjectsAPIListPagination


class ProjectsKwargsFilterView(ListAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Projects.objects.filter(title__contains=title)


# class ToDoAPIListPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


class ToDoAPIModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    #pagination_class = ToDoAPIListPagination


class ToDoKwargsFilterView(ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        projects = self.kwargs['proj']
        return ToDo.objects.filter(proj=projects)
