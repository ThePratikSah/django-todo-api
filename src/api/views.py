from rest_framework import viewsets
from todo.models import TodoItem
from .serializers import TodoSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
