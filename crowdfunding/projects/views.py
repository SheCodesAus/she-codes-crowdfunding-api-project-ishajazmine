# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Project
from .serializers import ProjectSerializer
# from crowdfunding.projects import serializers
# from crowdfunding.projects import serializers

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# whenever you make new table re-do a subset of this process

class ProjectDetail(APIView):

    def get_object(self, pk):
        return Project.objects.get(pk=pk)
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)