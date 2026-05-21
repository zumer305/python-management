from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Project
from .serializers import ProjectSerializer
from .filters import ProjectFilter

from .permissions import IsOwner
# Do not assign to the name `permission_classes` — it shadows the decorator
# Use the `@permission_classes([...])` decorator on view functions instead.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def project_list_create(request):

    if request.method == 'GET':

        projects = Project.objects.filter(created_by=request.user)

        #  FILTER + SEARCH + ORDERING setup
        filter_backend = DjangoFilterBackend()
        search_backend = SearchFilter()
        ordering_backend = OrderingFilter()

        queryset = filter_backend.filter_queryset(request, projects, view=None)
        queryset = search_backend.filter_queryset(request, queryset, view=None)
        queryset = ordering_backend.filter_queryset(request, queryset, view=None)

        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def project_detail(request, pk):

    try:
        project = Project.objects.get(pk=pk, created_by=request.user)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        project.delete()
        return Response({"message": "Project deleted"})
    





    