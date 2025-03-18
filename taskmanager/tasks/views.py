from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer # type: ignore
from rest_framework import filters
from django.core.cache import cache

scheduler = TaskScheduler()

class TaskViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        task = Task.objects.get(id=response.data['id'])
        scheduler.add_task(task)
        return response

    @action(detail=False, methods=['get'])
    def next_task(self, request):
        next_task = scheduler.get_next_task()
        if not next_task:
            return Response({'message': 'No tasks available'}, status=404)
        return Response(TaskSerializer(next_task).data)



import heapq

class TaskScheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        heapq.heappush(self.task_queue, (task.priority, task.created_at, task))

    def get_next_task(self):
        return heapq.heappop(self.task_queue)[2] if self.task_queue else None




