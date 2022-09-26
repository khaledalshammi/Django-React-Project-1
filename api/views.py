from rest_framework.decorators import api_view
from .serializers import TaskSerializers
from .models import Task
from rest_framework.response import Response

@api_view(['GET'])
def task_list(request):
    data = Task.objects.all().order_by('-id')
    serializer = TaskSerializers(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request,pk):
    data = Task.objects.get(pk=pk)
    serializer = TaskSerializers(data)
    return Response(serializer.data)

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request,pk):
    data = Task.objects.get(pk=pk)
    serializer = TaskSerializers(instance=data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request,pk):
    data = Task.objects.get(pk=pk)
    data.delete()
    return Response('deleted')