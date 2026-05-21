from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from projects.permissions import IsOwner

from .models import Task
from .serializers import TaskSerializer




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_create(request):

    if request.method == 'GET':

        tasks = Task.objects.filter(created_by=request.user)

        #  FILTER + SEARCH + ORDERING
        filter_backend = DjangoFilterBackend()
        search_backend = SearchFilter()
        ordering_backend = OrderingFilter()

        queryset = filter_backend.filter_queryset(request, tasks, view=None)
        queryset = search_backend.filter_queryset(request, queryset, view=None)
        queryset = ordering_backend.filter_queryset(request, queryset, view=None)

        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):

    try:
        task = Task.objects.get(pk=pk, created_by=request.user)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        task.delete()
        return Response({"message": "Task deleted"})


# Note: do not assign to the name `permission_classes` in module scope —
# it would shadow the decorator and cause `TypeError: 'list' object is not callable`.


