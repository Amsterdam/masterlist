import factory
from factory.django import DjangoModelFactory

from organization.models import (
    Contact,
    Customer,
    Organization,
    PersonalDataStatus,
    Team,
)
from organization.models import User as OrganizationUser
from project.models import (
    Project,
    ProjectStatus,
    ProjectType,
    SupportContractStatus,
    WpdDocumentStatus,
)


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Faker('text')


class ProjectTypeFactory(DjangoModelFactory):
    class Meta:
        model = ProjectType

    name = factory.Faker('text')


class ProjectStatusFactory(DjangoModelFactory):
    class Meta:
        model = ProjectStatus

    name = factory.Faker('text')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = OrganizationUser

    name = factory.Faker('name')


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Faker('text')


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    organization = factory.SubFactory(OrganizationFactory)


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    name = factory.Faker('text')


class SupportContractStatusFactory(DjangoModelFactory):
    class Meta:
        model = SupportContractStatus

    name = factory.Iterator(
        [
            "Lopend",
            "On hold",
            "Verkenning",
            "In ontwikkeling",
            "In beheer",
            "Beëindiging project/dienst (stekker eruit)",
            "Beëindiging project (dienst in beheer genomen)",
            "Administratief archiveren (3/3)",
            "te beeindigen (1/3)",
            "voor uren schrijven",
            "Beeindigd (2/3)",
            "Exploitatie",
            "Voorbereiding",
        ]
    )


class PersonalDataStatusFactory(DjangoModelFactory):
    class Meta:
        model = PersonalDataStatus

    name = factory.Faker('text')


class WpdDocumentStatusFactory(DjangoModelFactory):
    class Meta:
        model = WpdDocumentStatus

    name = factory.Faker('text')


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker('slug')
    project_number = factory.Faker('pyint')
    project_type = factory.SubFactory(ProjectTypeFactory)
    project_status = factory.SubFactory(ProjectStatusFactory)
    project_manager_user = factory.SubFactory(UserFactory)
    account_holder_user = factory.SubFactory(UserFactory)
    team = factory.SubFactory(TeamFactory)
    customer = factory.SubFactory(CustomerFactory)
    contact = factory.SubFactory(ContactFactory)
    support_contract_status = factory.SubFactory(SupportContractStatusFactory)
    support_contract_start = factory.Faker('date')
    support_contract_end = factory.Faker('date')
    personal_data_status = factory.SubFactory(PersonalDataStatusFactory)
    wpd_document_status = factory.SubFactory(WpdDocumentStatusFactory)
    wpd_completion_date = factory.Faker('date')
    privacy_status_updates = factory.Faker('text')
    description = factory.Faker('text')
    lijst_remco = factory.Faker('pyint')
    bio_quickscan_available = factory.Faker('boolean')
    bio_quickscan_path = factory.Faker('text')
