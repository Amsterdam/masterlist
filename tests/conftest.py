from pytest_factoryboy import register

from tests.project.factories import (
    ProjectFactory,
    SupportContractStatusFactory,
    WpdDocumentStatusFactory,
)

register(ProjectFactory)
register(WpdDocumentStatusFactory)
register(SupportContractStatusFactory)
