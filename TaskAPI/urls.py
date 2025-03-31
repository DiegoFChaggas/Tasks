from django.urls import path
from .views import TasksAPIView, TaskAPIView

urlpatterns = [
    path('tasks/', TasksAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskAPIView.as_view(), name='task'),
]