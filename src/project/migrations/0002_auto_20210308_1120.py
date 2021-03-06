# Generated by Django 3.1.5 on 2021-03-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lijst_remco',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='old_project_numbers',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='personal_data_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organization.personaldatastatus'),
        ),
        migrations.AlterField(
            model_name='project',
            name='privacy_status_updates',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
