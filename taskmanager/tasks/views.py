from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer # type: ignore

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-priority', 'created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

