from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from .serializers import ProjectSerializer, ToDoSerializer
from .models import Project, ToDo


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    pagination_class = ProjectLimitOffsetPagination


def get_queryset(self):
    name = self.request.query_params.get('name', '')
    projects = Project.objects.all
    if name:
        projects = projects.filter(name__contains=name)

    return projects

class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination

    filterset_fields = ['project_id']