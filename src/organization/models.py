from django.db import models


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
