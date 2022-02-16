from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    project_number = models.BigIntegerField()
    old_project_numbers = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(
        'organization.Team', models.SET_NULL, blank=True, null=True
    )
    infrastructure_segment = models.ForeignKey(
        'infra.InfrastructureSegment', models.SET_NULL, blank=True, null=True
    )
    customer = models.ForeignKey(
        'organization.Customer', models.SET_NULL, blank=True, null=True
    )
    customer_id_source = models.CharField(max_length=255, blank=True, null=True)
    contact = models.ForeignKey(
        'organization.Contact', models.SET_NULL, blank=True, null=True
    )
    project_type = models.ForeignKey(
        'ProjectType', models.SET_NULL, blank=True, null=True
    )
    project_status = models.ForeignKey(
        'ProjectStatus', models.SET_NULL, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    support_contract_status = models.ForeignKey(
        'SupportContractStatus', models.SET_NULL, blank=True, null=True
    )
    support_contract_start = models.DateField(blank=True, null=True)
    support_contract_end = models.DateField(blank=True, null=True)
    support_contract_document_path = models.CharField(
        max_length=255, blank=True, null=True
    )
    project_manager_user = models.ForeignKey(
        'organization.User',
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='projects_manager',
    )
    account_holder_user = models.ForeignKey(
        'organization.User',
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='projects_account_holder',
    )
    description = models.TextField(blank=True, null=True)
    privacy_officer = models.ForeignKey(
        'organization.PrivacyOfficer', models.SET_NULL, blank=True, null=True
    )
    security_officer = models.ForeignKey(
        'organization.SecurityOfficer', models.SET_NULL, blank=True, null=True
    )
    information_manager = models.ForeignKey(
        'organization.InformationManager', models.SET_NULL, blank=True, null=True
    )
    personal_data_status = models.ForeignKey(
        'organization.PersonalDataStatus', models.SET_NULL, blank=True, null=True
    )
    wpd_completion_date = models.DateField(blank=True, null=True)
    wpd_document_status = models.ForeignKey(
        'WpdDocumentStatus', models.SET_NULL, blank=True, null=True
    )
    path_wpd_document = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    path_release_document = models.CharField(max_length=255, blank=True, null=True)
    destroy_date = models.DateField(blank=True, null=True)
    path_destroy_document = models.CharField(max_length=255, blank=True, null=True)
    security_availability_level = models.ForeignKey(
        'SecurityAvailabilityLevel', models.SET_NULL, blank=True, null=True
    )
    security_integrity_level = models.ForeignKey(
        'SecurityIntegrityLevel', models.SET_NULL, blank=True, null=True
    )
    security_confidentiality_level = models.ForeignKey(
        'SecurityConfidentialityLevel', models.SET_NULL, blank=True, null=True
    )
    bio_quickscan_available = models.BooleanField(default=False, blank=True, null=True)
    bio_quickscan_path = models.CharField(max_length=255, blank=True, null=True)
    security_scan_required = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    security_scan_date = models.DateField(blank=True, null=True)
    path_security_scan_document = models.CharField(
        max_length=255, blank=True, null=True
    )
    authorization_granter_email = models.CharField(
        max_length=255, blank=True, null=True
    )
    path_authorization_matrix_document = models.CharField(
        max_length=255, blank=True, null=True
    )
    privacy_status_updates = models.TextField(blank=True, null=True)
    lijst_remco = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class ProjectType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class SecurityAvailabilityLevel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class SecurityConfidentialityLevel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class SecurityIntegrityLevel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class SupportContractStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class WpdDocumentStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
