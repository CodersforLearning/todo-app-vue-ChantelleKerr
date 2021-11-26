from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/tasks/',
            'method': 'GET',
        },
        {
            'Endpoint': '/tasks/create',
            'method': 'POST',
        },
        {
            'Endpoint': '/task/<str:pk>',
            'method': 'PUT',
        },
        {
            'Endpoint': '/task/delete/<str:pk>',
            'method': 'DELETE',
        },
        
    ]
    return Response(routes)
# Create your views here.
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def remove_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task Deleted')


