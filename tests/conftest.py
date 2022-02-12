from pytest_factoryboy import register

from tests.project.factories import (
    ContactFactory,
    CustomerFactory,
    OrganizationFactory,
    PersonalDataStatusFactory,
    ProjectFactory,
    ProjectStatusFactory,
    ProjectTypeFactory,
    SupportContractStatusFactory,
    TeamFactory,
    UserFactory,
    WpdDocumentStatusFactory,
)

register(ContactFactory)
register(CustomerFactory)
register(OrganizationFactory)
register(PersonalDataStatusFactory)
register(ProjectFactory)
register(ProjectStatusFactory)
register(ProjectTypeFactory)
register(SupportContractStatusFactory)
register(TeamFactory)
register(UserFactory)
register(WpdDocumentStatusFactory)
