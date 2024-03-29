# Generated by Django 4.0.1 on 2022-02-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210311_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bio_quickscan_available',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='bio_quickscan_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
