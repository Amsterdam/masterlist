from django.db.models import Manager

from project.querysets import ProjectQuerySet


class ProjectManager(Manager.from_queryset(ProjectQuerySet)):
    def get_queryset(self):
        return super().get_queryset().select_related('team')
