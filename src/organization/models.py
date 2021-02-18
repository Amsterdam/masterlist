from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        'Organization', models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class LegalBase(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class PersonalDataStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class PrivacyOfficer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class InformationManager(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class SecurityOfficer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(
        'Organization', models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
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

    def __str__(self):
        return f"{self.name}"
