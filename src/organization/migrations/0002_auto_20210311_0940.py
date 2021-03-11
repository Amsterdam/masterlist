# Generated by Django 3.1.5 on 2021-03-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='securityofficer',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='team',
            name='product_owner_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams_product_owner', to='organization.user'),
        ),
        migrations.AlterField(
            model_name='team',
            name='scrum_master_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams_scrum_master', to='organization.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.team'),
        ),
    ]
