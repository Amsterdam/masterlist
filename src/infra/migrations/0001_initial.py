# Generated by Django 3.1.5 on 2021-01-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hash', models.CharField(max_length=255)),
                ('container_name', models.CharField(max_length=255)),
                ('first_seen', models.DateTimeField()),
                ('last_seen', models.DateTimeField()),
            ],
            options={
                'db_table': 'containers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'databases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabaseCluster',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'database_clusters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabaseInstance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'database_instances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabaseName',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'database_names',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabasePermission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'database_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabasePermissionTeamAuthorization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('authorization_granter_email', models.CharField(max_length=255)),
                ('granted_from', models.DateField()),
                ('granted_untill', models.DateField()),
            ],
            options={
                'db_table': 'database_permission_team_authorizations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabasePermissionUserAuthorization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('authorization_granter_email', models.CharField(max_length=255)),
                ('granted_from', models.DateField()),
                ('granted_untill', models.DateField()),
            ],
            options={
                'db_table': 'database_permission_user_authorizations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('customer_text', models.CharField(max_length=255)),
                ('first_seen', models.DateTimeField(blank=True, null=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'domains',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfrastructureSegment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('letter', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=255)),
                ('consul_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'infrastructure_segments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('ip_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'servers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
    ]
