# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status, permissions
from .models import Project, Pledge, Category
from .serializers import CategorySerializer, ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from .permissions import IsOwnerOrReadOnly
# from crowdfunding.projects import serializers
# from crowdfunding.projects import serializers

# CREATE NEW VIEW FOR PLEDGE LIST
class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        order_by = request.query_params.get('order_by', None)
        if order_by:
            pledges = pledges.order_by(order_by)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # is autoenticated wont let post but can let us see. if just is authenticated and will not let you get or post
    # want to see project list but can't change unless we're logged in. 

    def get(self, request):
        projects = Project.objects.all()
        is_open = request.query_params.get('is_open', None)
        if is_open:
            projects = projects.filter(is_open=is_open)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            # return Response(serializer.data)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )


# whenever you make new table re-do a subset of this process

class ProjectDetail(APIView):
    # only logged in can edit all projects. all can view projects
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            # return Project.objects.get(pk=pk)
            project =Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            return project
        except Project.DoesNotExist:
            raise Http404    
        # return Project.objects.get(pk=pk)
    
    def get(self, request, pk):
        project = self.get_object(pk)
        # serializer = ProjectSerializer(project)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    # def post(self, request, pk):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
