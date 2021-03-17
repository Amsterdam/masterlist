from pytest_factoryboy import register

from tests.project.factories import ProjectFactory, WpdDocumentStatusFactory

register(ProjectFactory)
register(WpdDocumentStatusFactory)
