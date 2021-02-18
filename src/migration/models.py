from django.db import models


class DatabaseInstance(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    database_cluster = models.ForeignKey(
        'DatabaseCluster', models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = 'database_instances'
        managed = False

    def __str__(self):
        return f"{self.name}"


class DatabaseName(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'database_names'
        managed = False
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class DatabasePermissionTeamAuthorization(models.Model):
    id = models.BigAutoField(primary_key=True)
    database_permission = models.ForeignKey('DatabasePermission', models.DO_NOTHING)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    legal_basis = models.ForeignKey('LegalBase', models.DO_NOTHING)
    reason = models.TextField()
    authorization_granter_email = models.CharField(max_length=255)
    granted_from = models.DateField()
    granted_untill = models.DateField()

    class Meta:
        db_table = 'database_permission_team_authorizations'
        managed = False

    def __str__(self):
        return f"{self.database_permission}"


class DatabasePermissionUserAuthorization(models.Model):
    id = models.BigAutoField(primary_key=True)
    database_permission = models.ForeignKey('DatabasePermission', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    legal_basis = models.ForeignKey('LegalBase', models.DO_NOTHING)
    reason = models.TextField()
    authorization_granter_email = models.CharField(max_length=255)
    granted_from = models.DateField()
    granted_untill = models.DateField()

    class Meta:
        db_table = 'database_permission_user_authorizations'
        managed = False

    def __str__(self):
        return f"{self.database_permission}"


class DatabasePermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    database_name = models.ForeignKey(
        'DatabaseName', models.DO_NOTHING, blank=True, null=True
    )
    description = models.TextField()

    class Meta:
        db_table = 'database_permissions'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Database(models.Model):
    id = models.BigAutoField(primary_key=True)
    database_name = models.ForeignKey('DatabaseName', models.DO_NOTHING)
    database_cluster = models.ForeignKey('DatabaseCluster', models.DO_NOTHING)

    class Meta:
        db_table = 'databases'
        managed = False

    def __str__(self):
        return f"{self.database_name} ({self.database_cluster})"


class Domain(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    customer_text = models.CharField(max_length=255)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'domains'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Container(models.Model):
    id = models.BigAutoField(primary_key=True)
    server = models.ForeignKey('Server', models.DO_NOTHING, blank=True, null=True)
    hash = models.CharField(max_length=255)
    container_name = models.CharField(max_length=255)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()

    class Meta:
        db_table = 'containers'
        managed = False

    def __str__(self):
        return f"{self.container_name}"


class InfrastructureSegment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    letter = models.CharField(max_length=2)
    description = models.CharField(max_length=255)
    consul_url = models.URLField(max_length=255)

    class Meta:
        db_table = 'infrastructure_segments'
        managed = False

    def __str__(self):
        return f"{self.name}"


class DatabaseCluster(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'database_clusters'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Server(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    infrastructure_segment = models.ForeignKey(
        'InfrastructureSegment', models.DO_NOTHING
    )
    hostname = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'servers'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    infrastructure_segment = models.ForeignKey(
        'InfrastructureSegment', models.DO_NOTHING, blank=True, null=True
    )
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'services'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    project_number = models.BigIntegerField(blank=True, null=True)
    old_project_numbers = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    infrastructure_segment = models.ForeignKey(
        'InfrastructureSegment', models.DO_NOTHING, blank=True, null=True
    )
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    customer_id_source = models.CharField(max_length=255, blank=True, null=True)
    contact = models.ForeignKey('Contact', models.DO_NOTHING, blank=True, null=True)
    project_type = models.ForeignKey(
        'ProjectType', models.DO_NOTHING, blank=True, null=True
    )
    project_status = models.ForeignKey(
        'ProjectStatus', models.DO_NOTHING, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    support_contract_status = models.ForeignKey(
        'SupportContractStatus', models.DO_NOTHING, blank=True, null=True
    )
    support_contract_start = models.DateField(blank=True, null=True)
    support_contract_end = models.DateField(blank=True, null=True)
    support_contract_document_path = models.CharField(
        max_length=255, blank=True, null=True
    )
    project_manager_user = models.ForeignKey(
        'User',
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='projects_manager',
    )
    account_holder_user = models.ForeignKey(
        'User',
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='projects_account_holder',
    )
    description = models.TextField(blank=True, null=True)
    privacy_officer = models.ForeignKey(
        'PrivacyOfficer', models.DO_NOTHING, blank=True, null=True
    )
    security_officer = models.ForeignKey(
        'SecurityOfficer', models.DO_NOTHING, blank=True, null=True
    )
    information_manager = models.ForeignKey(
        'InformationManager', models.DO_NOTHING, blank=True, null=True
    )
    personal_data_status = models.ForeignKey('PersonalDataStatus', models.DO_NOTHING)
    wpd_completion_date = models.DateField(blank=True, null=True)
    wpd_document_status = models.ForeignKey(
        'WpdDocumentStatus', models.DO_NOTHING, blank=True, null=True
    )
    path_wpd_document = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    path_release_document = models.CharField(max_length=255, blank=True, null=True)
    destroy_date = models.DateField(blank=True, null=True)
    path_destroy_document = models.CharField(max_length=255, blank=True, null=True)
    security_availability_level = models.ForeignKey(
        'SecurityAvailabilityLevel', models.DO_NOTHING, blank=True, null=True
    )
    security_integrity_level = models.ForeignKey(
        'SecurityIntegrityLevel', models.DO_NOTHING, blank=True, null=True
    )
    security_confidentiality_level = models.ForeignKey(
        'SecurityConfidentialityLevel', models.DO_NOTHING, blank=True, null=True
    )
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
    privacy_status_updates = models.TextField()
    lijst_remco = models.BigIntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'projects'
        managed = False


class ProjectStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'project_status'
        managed = False

    def __str__(self):
        return f"{self.name}"


class ProjectType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'project_types'
        managed = False

    def __str__(self):
        return f"{self.name}"


class SecurityAvailabilityLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'security_availability_levels'
        managed = False

    def __str__(self):
        return f"{self.name}"


class SecurityConfidentialityLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'security_confidentiality_levels'
        managed = False

    def __str__(self):
        return f"{self.name}"


class SecurityIntegrityLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'security_integrity_levels'
        managed = False

    def __str__(self):
        return f"{self.name}"


class SupportContractStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'support_contract_status'
        managed = False

    def __str__(self):
        return f"{self.name}"


class WpdDocumentStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'wpd_document_status'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Organization(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizations'
        managed = False

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'users'
        managed = False

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'contacts'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        'Organization', models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = 'customers'
        managed = False

    def __str__(self):
        return f"{self.name}"


class LegalBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'legal_bases'
        managed = False

    def __str__(self):
        return f"{self.name}"


class PersonalDataStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'personal_data_status'
        managed = False

    def __str__(self):
        return f"{self.name}"


class PrivacyOfficer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'privacy_officers'
        managed = False

    def __str__(self):
        return f"{self.name}"


class InformationManager(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'information_managers'
        managed = False

    def __str__(self):
        return f"{self.name}"


class SecurityOfficer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(
        'Organization', models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        db_table = 'security_officers'
        managed = False

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    product_owner_user = models.ForeignKey(
        'User',
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='teams_product_owner',
    )
    scrum_master_user = models.ForeignKey(
        'User',
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='teams_scrum_master',
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'teams'
        managed = False

    def __str__(self):
        return f"{self.name}"
