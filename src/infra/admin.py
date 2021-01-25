from django.contrib import admin

from . import models

default_models = [
    models.Domain,
    models.DatabaseCluster,
    models.Server,
]

for i in default_models:
    admin.site.register(i)


@admin.register(models.Container)
class ContainerAdmin(admin.ModelAdmin):
    search_fields = ['container_name']
    list_display = ['container_name', 'server', 'first_seen', 'last_seen']
    list_filter = [
        'first_seen',
        'last_seen',
    ]


@admin.register(models.Database)
class DatabaseAdmin(admin.ModelAdmin):
    ordering = ['database_name__name']
    list_select_related = ['database_name', 'database_cluster']
    search_fields = ['database_name']
    list_display = ['database_name', 'database_cluster']
    list_filter = ['database_cluster']


@admin.register(models.DatabaseInstance)
class DatabaseInstanceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'database_cluster']
    list_filter = ['database_cluster']


@admin.register(models.InfrastructureSegment)
class InfrastructureSegmentAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.DatabaseName)
class DatabaseNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'project']
    autocomplete_fields = ['project']
    search_fields = ['name']


@admin.register(models.DatabasePermissionTeamAuthorization)
class DatabasePermissionTeamAuthorizationAdmin(admin.ModelAdmin):
    list_display = [
        'database_permission',
        'team',
        'legal_basis',
        'granted_from',
        'granted_untill',
    ]


@admin.register(models.DatabasePermissionUserAuthorization)
class DatabasePermissionUserAuthorizationAdmin(admin.ModelAdmin):
    list_display = [
        'database_permission',
        'user',
        'legal_basis',
        'granted_from',
        'granted_untill',
    ]


@admin.register(models.DatabasePermission)
class DatabasePermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'database_name']
    search_fields = ['name', 'database_name__name']


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    list_display = [
        'active',
        'name',
        'infrastructure_segment',
        'project',
    ]
    list_filter = [
        'active',
        'infrastructure_segment',
    ]
    autocomplete_fields = ['project']
