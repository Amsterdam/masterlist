from django.contrib import admin
from django.db.models import F

from util.csv import CSVExport

from . import models

default_models = [
    models.ProjectStatus,
    models.SecurityAvailabilityLevel,
    models.SecurityConfidentialityLevel,
    models.SecurityIntegrityLevel,
    models.SupportContractStatus,
    models.WpdDocumentStatus,
]

for i in default_models:
    admin.site.register(i)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name', 'project_number')
    autocomplete_fields = [
        'customer',
        'contact',
        'project_manager_user',
        'account_holder_user',
    ]
    list_display = (
        'name',
        'project_number',
        'team',
        'customer',
    )
    list_filter = ['team', 'project_status', 'personal_data_status']
    radio_fields = {
        'project_status': admin.VERTICAL,
        'support_contract_status': admin.VERTICAL,
        'personal_data_status': admin.VERTICAL,
        'wpd_document_status': admin.VERTICAL,
        'security_availability_level': admin.VERTICAL,
        'security_integrity_level': admin.VERTICAL,
        'security_confidentiality_level': admin.VERTICAL,
    }

    actions = ['export_csv']

    def export_csv(self, request, qs):
        csv_export = CSVExport(encoding='utf-8-sig', delimiter=';')
        # We use F values here to control the order
        qs = qs.values('id').annotate(
            name=F('name'),
            project_number=F('project_number'),
            project_name=F('name'),
            project_type=F('project_type__name'),
            project_status=F('project_status__name'),
            project_manager=F('project_manager_user__name'),
            account_holder=F('account_holder_user__name'),
            team_name=F('team__name'),
            organization_name=F('customer__organization__name'),
            contact_name=F('contact__name'),
            support_contract_status=F('support_contract_status__name'),
            support_contract_start=F('support_contract_start'),
            support_contract_end=F('support_contract_end'),
            personal_data_status=F('personal_data_status__name'),
            wpd_document_status=F('wpd_document_status__name'),
            wpd_completion_date=F('wpd_completion_date'),
            privacy_status_updates=F('privacy_status_updates'),
            project_description=F('description'),
            lijst_remco=F('lijst_remco'),
        )
        return csv_export.export("export", qs.iterator(), download=True)
