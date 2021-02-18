from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.utils import IntegrityError

from infra import models as infra
from migration import models as old
from organization import models as organization
from project import models as project

mapping = {
    old.Team: organization.Team,
    old.User: organization.User,
    old.Project: project.Project,
    old.ProjectStatus: project.ProjectStatus,
    old.ProjectType: project.ProjectType,
    old.SecurityAvailabilityLevel: project.SecurityAvailabilityLevel,
    old.SecurityConfidentialityLevel: project.SecurityConfidentialityLevel,
    old.SecurityIntegrityLevel: project.SecurityIntegrityLevel,
    old.SupportContractStatus: project.SupportContractStatus,
    old.WpdDocumentStatus: project.WpdDocumentStatus,
    old.Container: infra.Container,
    old.Database: infra.Database,
    old.DatabaseCluster: infra.DatabaseCluster,
    old.DatabaseInstance: infra.DatabaseInstance,
    old.DatabaseName: infra.DatabaseName,
    old.DatabasePermission: infra.DatabasePermission,
    old.DatabasePermissionTeamAuthorization: infra.DatabasePermissionTeamAuthorization,
    old.DatabasePermissionUserAuthorization: infra.DatabasePermissionUserAuthorization,
    old.Domain: infra.Domain,
    old.InfrastructureSegment: infra.InfrastructureSegment,
    old.Server: infra.Server,
    old.Service: infra.Service,
    old.Customer: organization.Customer,
    old.Contact: organization.Contact,
    old.LegalBase: organization.LegalBase,
    old.Organization: organization.Organization,
    old.PrivacyOfficer: organization.PrivacyOfficer,
    old.SecurityOfficer: organization.SecurityOfficer,
    old.InformationManager: organization.InformationManager,
    old.PersonalDataStatus: organization.PersonalDataStatus,
}


class Command(BaseCommand):
    help = 'Copy the data from the unmanaged to the managed models'

    def handle(self, *args, **options):
        with transaction.atomic():
            for source, destination in mapping.items():
                self.stdout.write(self.style.MIGRATE_HEADING('-' * 80))
                self.stdout.write("Source: " + self.style.MIGRATE_LABEL(source))
                self.stdout.write(
                    "Destination: " + self.style.MIGRATE_LABEL(destination)
                )
                destination.objects.filter().delete()
                records = []
                rows = source.objects.filter()
                for row in rows:
                    data = row.__dict__
                    if '_state' in data:
                        data.pop('_state')
                    records.append(destination(**data))

                self.stdout.write(f"Number of rows: {len(records)}")
                for record in records:
                    record.save()
