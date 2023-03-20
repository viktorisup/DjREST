from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from todoapp.serializers import ProjectSerializer, ToDoSerializer
from todoapp.models import Project, ToDo
# from .filters import ProjectFilter, TodoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    pagination_class = ProjectLimitOffsetPagination
    # filterset_class = ProjectFilter


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
    # filterset_class = TodoFilter

    filterset_fields = ['project_id']

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()