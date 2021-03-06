# Generated by Django 3.1.5 on 2021-02-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('infra', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
        migrations.AddField(
            model_name='server',
            name='infrastructure_segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infra.infrastructuresegment'),
        ),
        migrations.AddField(
            model_name='domain',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organization.customer'),
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
        migrations.AddField(
            model_name='databasepermissionuserauthorization',
            name='database_permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasepermission'),
        ),
        migrations.AddField(
            model_name='databasepermissionuserauthorization',
            name='legal_basis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.legalbase'),
        ),
        migrations.AddField(
            model_name='databasepermissionuserauthorization',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.user'),
        ),
        migrations.AddField(
            model_name='databasepermissionteamauthorization',
            name='database_permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasepermission'),
        ),
        migrations.AddField(
            model_name='databasepermissionteamauthorization',
            name='legal_basis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.legalbase'),
        ),
        migrations.AddField(
            model_name='databasepermissionteamauthorization',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.team'),
        ),
        migrations.AddField(
            model_name='databasepermission',
            name='database_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasename'),
        ),
        migrations.AddField(
            model_name='databasename',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
        migrations.AddField(
            model_name='databaseinstance',
            name='database_cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasecluster'),
        ),
        migrations.AddField(
            model_name='database',
            name='database_cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasecluster'),
        ),
        migrations.AddField(
            model_name='database',
            name='database_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infra.databasename'),
        ),
        migrations.AddField(
            model_name='container',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infra.server'),
        ),
    ]
