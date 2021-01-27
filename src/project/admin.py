from django.contrib import admin

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
