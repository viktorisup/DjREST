from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User
class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

class UserSerializerVersionTwo(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_staff", "is_superuser"]