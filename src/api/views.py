from rest_framework.viewsets import ModelViewSet

from apps.todo.models import ToDo

from .serializers import ToDoSerializer, ToDoListSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    list_serializer_class = ToDoListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return self.serializer_class
