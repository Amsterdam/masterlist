import operator
from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView

from organization.models import Team
from project.models import Project


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search/results.html"
    lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '@': 'search',
        '$': 'iregex',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_terms = self.get_search_terms(self.request)

        search_fields_mapping = dict(
            projects=dict(
                model=Project,
                fields=['name', 'project_number', 'team__name'],
            ),
            teams=dict(
                model=Team,
                fields=['name'],
            ),
        )

        title = _('Results for')
        context['title'] = f"{title}: {' '.join(search_terms)}"

        for key, mapping in search_fields_mapping.items():
            orm_lookups = [
                self.construct_search(str(field)) for field in mapping['fields']
            ]
            conditions = []
            for term in search_terms:
                queries = [models.Q(**{lookup: term}) for lookup in orm_lookups]
                conditions.append(reduce(operator.or_, queries))
            qs = mapping['model'].objects.filter(reduce(operator.and_, conditions))
            context[key] = qs

        return context

    def construct_search(self, field_name):
        lookup = self.lookup_prefixes.get(field_name[0])
        if lookup:
            field_name = field_name[1:]
        else:
            lookup = 'icontains'
        return LOOKUP_SEP.join([field_name, lookup])

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.GET.get('search')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        return params.split()
