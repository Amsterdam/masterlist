from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import ListView

from project.models import Project


class ProjectView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = _('Projects')
        context['subtitle'] = _('List')

        return context
