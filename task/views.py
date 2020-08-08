from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import TaskTracker, Task


# Serializers Start
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
        fields = '__all__'


class TaskTrackerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize the Tasks
    """
    class Meta:
        model = TaskTracker
        fields = '__all__'


# Views Start
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskTrackerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'task', TaskViewSet)
router.register(r'track', TaskTrackerViewSet)
