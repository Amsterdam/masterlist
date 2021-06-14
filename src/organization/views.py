from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import ListView

from organization.models import Team


class TeamsView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = _('Teams')

        return context
