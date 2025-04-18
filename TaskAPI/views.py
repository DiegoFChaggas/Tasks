from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TasksAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
