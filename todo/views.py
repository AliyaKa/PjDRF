from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from .models import Projects, ToDo
from .serializers import ProjectsSerializer, ToDoSerializer
from rest_framework.response import Response


class ProjectsAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Projects.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ProjectsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ToDoAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = ToDo.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ToDoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


