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
        assert row['project_number'] == str(project.project_number)
        assert row['name'] == project.name
        assert row['wpd_document_status'] == project.wpd_document_status.name
        assert row['wpd_completion_date'] == project.wpd_completion_date
        assert row['privacy_status_updates'] == project.privacy_status_updates
        assert row['project_description'] == project.description
        assert row['support_contract_status'] == project.support_contract_status.name
        assert row['support_contract_start'] == project.support_contract_start
        assert row['support_contract_end'] == project.support_contract_end
