import factory
from factory.django import DjangoModelFactory

from project.models import Project, SupportContractStatus, WpdDocumentStatus


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


class WpdDocumentStatusFactory(DjangoModelFactory):
    class Meta:
        model = WpdDocumentStatus

    name = factory.Faker('text')


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker('slug')
    project_number = factory.Faker('pyint')
    privacy_status_updates = factory.Faker('text')
    description = factory.Faker('text')

    wpd_completion_date = factory.Faker('date')
    wpd_document_status = factory.SubFactory(WpdDocumentStatusFactory)

    support_contract_status = factory.SubFactory(SupportContractStatusFactory)
    support_contract_start = factory.Faker('date')
    support_contract_end = factory.Faker('date')
