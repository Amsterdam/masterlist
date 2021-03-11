from django.db import models


class DatabaseInstance(models.Model):
    name = models.CharField(unique=True, max_length=255)
    database_cluster = models.ForeignKey(
        'DatabaseCluster', models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class DatabaseName(models.Model):
    name = models.CharField(unique=True, max_length=255)
    project = models.ForeignKey(
        'project.Project', models.SET_NULL, blank=True, null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class DatabasePermissionTeamAuthorization(models.Model):
    database_permission = models.ForeignKey('DatabasePermission', models.SET_NULL, blank=True, null=True)
    team = models.ForeignKey('organization.Team', models.SET_NULL, blank=True, null=True)
    legal_basis = models.ForeignKey('organization.LegalBase', models.SET_NULL, blank=True, null=True)
    reason = models.TextField()
    authorization_granter_email = models.CharField(max_length=255)
    granted_from = models.DateField()
    granted_untill = models.DateField()

    def __str__(self):
        return f"{self.database_permission}"


class DatabasePermissionUserAuthorization(models.Model):
    database_permission = models.ForeignKey('DatabasePermission', models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey('organization.User', models.SET_NULL, blank=True, null=True)
    legal_basis = models.ForeignKey('organization.LegalBase', models.SET_NULL, blank=True, null=True)
    reason = models.TextField()
    authorization_granter_email = models.CharField(max_length=255)
    granted_from = models.DateField()
    granted_untill = models.DateField()

    def __str__(self):
        return f"{self.database_permission}"


class DatabasePermission(models.Model):
    name = models.CharField(unique=True, max_length=255)
    database_name = models.ForeignKey(
        'DatabaseName', models.SET_NULL, blank=True, null=True
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Database(models.Model):
    database_name = models.ForeignKey('DatabaseName', models.SET_NULL, blank=True, null=True)
    database_cluster = models.ForeignKey('DatabaseCluster', models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.database_name} ({self.database_cluster})"


class Domain(models.Model):
    name = models.CharField(max_length=255)
    customer_text = models.CharField(max_length=255)
    customer = models.ForeignKey(
        'organization.Customer', models.SET_NULL, blank=True, null=True
    )
    project = models.ForeignKey(
        'project.Project', models.SET_NULL, blank=True, null=True
    )
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Container(models.Model):
    server = models.ForeignKey('Server', models.SET_NULL, blank=True, null=True)
    hash = models.CharField(max_length=255)
    container_name = models.CharField(max_length=255)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()

    def __str__(self):
        return f"{self.container_name}"


class InfrastructureSegment(models.Model):
    name = models.CharField(max_length=255)
    letter = models.CharField(max_length=2)
    description = models.CharField(max_length=255)
    consul_url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class DatabaseCluster(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Server(models.Model):
    name = models.CharField(max_length=255)
    infrastructure_segment = models.ForeignKey(
        'InfrastructureSegment', models.SET_NULL, blank=True, null=True
    )
    hostname = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    infrastructure_segment = models.ForeignKey(
        'InfrastructureSegment', models.SET_NULL, blank=True, null=True
    )
    project = models.ForeignKey(
        'project.Project', models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"
