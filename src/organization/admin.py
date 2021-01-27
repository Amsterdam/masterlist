from django.contrib import admin

from . import models

default_models = [
    models.Organization,
]

for i in default_models:
    admin.site.register(i)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'product_owner_user', 'scrum_master_user']
    autocomplete_fields = ['scrum_master_user', 'product_owner_user']


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'team__name']
    autocomplete_fields = ['team']
    list_display = ['name', 'team']
    list_filter = [
        'team',
    ]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'organization']
    list_filter = [
        'organization',
    ]


@admin.register(models.SecurityOfficer)
class SecurityOfficerAdmin(admin.ModelAdmin):
    list_select_related = ['organization']
    search_fields = ['name']
    list_display = ['name', 'organization']


@admin.register(models.PrivacyOfficer)
class PrivacyOfficerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name',
    ]


@admin.register(models.InformationManager)
class InformationManagerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name',
    ]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'customer', 'role']
    autocomplete_fields = ['customer']


@admin.register(models.LegalBase)
class LegalBaseAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.PersonalDataStatus)
class PersonalDataStatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
