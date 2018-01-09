# Generated by Django 2.0 on 2018-01-09 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ownership.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenantName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TenantLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ownership.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonInCharge',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('office_number', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ownership.CustomerLocation')),
            ],
            options={
                'abstract': False,
            },
            bases=('Ownership.user',),
        ),
        migrations.CreateModel(
            name='TenantPersonIncharge',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('office_number', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ownership.TenantLocation')),
            ],
            options={
                'abstract': False,
            },
            bases=('Ownership.user',),
        ),
        migrations.CreateModel(
            name='XMTStaff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('staffID', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('staffName', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ownership.Department')),
            ],
            options={
                'abstract': False,
            },
            bases=('Ownership.user',),
        ),
    ]
