from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import TaskTracker, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialise the User Views
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize the Tasks
    """
    class Meta:
        model = Task


# Views Start
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
