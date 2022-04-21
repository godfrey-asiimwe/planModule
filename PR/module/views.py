from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Project
from .serlializers import ProjectSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_projects': '/',
        'view Project': '/view/pk',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_projects(request):
    project = ProjectSerializer(data=request.data)

    # validating for already existing data
    if Project.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if project.is_valid():
        project.save()
        return Response(project.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_projects(request):
    # checking for the parameters from the URL
    projects = Project.objects.all()

    if projects:
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_ProjectByID(request, pk):
    # checking for the parameters from the URL
    project = Project.objects.get(pk=pk)

    if project:
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_projects(request, pk):
    project = Project.objects.get(pk=pk)
    data = ProjectSerializer(instance=project, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
