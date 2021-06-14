from rest_framework import viewsets

from api.projects.serializers import ProjectSerializer
from project.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['team']
    search_fields = ['name', 'project_number']
