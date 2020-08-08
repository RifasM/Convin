from django.contrib.auth.models import User
from djcelery.admin_utils import action
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

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

    @action(detail=True,
            methods=['put'],
            name='Update Task',
            short_description="Update the Task View")
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.task_type = request.data.get("task_type")
        instance.update_type = request.data.get("update_type")
        instance.email = request.data.get("email")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


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
