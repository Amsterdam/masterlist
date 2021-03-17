import factory
from factory.django import DjangoModelFactory

from project.models import Project, WpdDocumentStatus


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
