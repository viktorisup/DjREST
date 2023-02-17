from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import User
from .serializers import UserSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer]
    pagination_class = UserLimitOffsetPagination


def list(self, request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


