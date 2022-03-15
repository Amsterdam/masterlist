import csv
import io

import pytest
from django.contrib.admin.sites import AdminSite

from project.admin import ProjectAdmin
from project.models import Project


class MockRequest(object):
    def __init__(self, user=None):
        self.user = user


@pytest.mark.django_db
class TestAdminExport:
    def test_csv_export(self, project):
        project_admin = ProjectAdmin(model=Project, admin_site=AdminSite())
        response = project_admin.export_csv(
            request=MockRequest(), qs=Project.objects.all()
        )
        assert 'export_csv' in ProjectAdmin.actions
        assert response.charset == 'utf-8-sig'
        assert response.content.startswith(''.encode('utf-8-sig'))

        content = '\n'.join(
            map(lambda x: x.decode('utf-8-sig'), response.content.splitlines())
        )
        reader = csv.DictReader(io.StringIO(content), delimiter=';')
        rows = list(reader)

        row = rows[0]
        assert row['id'] == str(project.pk)
        assert row['name'] == project.name
        assert row['asset_id'] == (project.asset_id or "")
        assert row['project_number'] == str(project.project_number)
        assert row['project_type'] == project.project_type.name
        assert row['project_status'] == project.project_status.name
        assert row['project_manager'] == project.project_manager_user.name
        assert row['account_holder'] == project.account_holder_user.name
        assert row['team_name'] == project.team.name
        assert row['organization_name'] == project.customer.organization.name
        assert row['contact_name'] == project.contact.name
        assert row['support_contract_status'] == project.support_contract_status.name
        assert row['support_contract_start'] == project.support_contract_start
        assert row['support_contract_end'] == project.support_contract_end
        assert row['personal_data_status'] == project.personal_data_status.name
        assert row['wpd_document_status'] == project.wpd_document_status.name
        assert row['wpd_completion_date'] == project.wpd_completion_date
        assert row['privacy_status_updates'] == project.privacy_status_updates
        assert row['project_description'] == project.description
        assert row['lijst_remco'] == str(project.lijst_remco)
        assert row['bio_quickscan_available'] == str(project.bio_quickscan_available)
        assert row['bio_quickscan_path'] == project.bio_quickscan_path
