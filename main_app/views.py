from .serializers import ProjectSerializer, BugSerializer, CommentSerializer
from .models import Project, Bug, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BugViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer