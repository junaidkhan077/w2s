# Generated by Django 2.1.2 on 2020-02-27 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('created_by', models.IntegerField(blank=True, null=True, verbose_name='Created By')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created At')),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='Modified By')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='Modified At')),
            ],
            options={
                'db_table': 'City_Mstr',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('created_by', models.IntegerField(blank=True, null=True, verbose_name='Created By')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created At')),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='Modified By')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='Modified At')),
            ],
            options={
                'db_table': 'Province_Mstr',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='last_name')),
                ('primary_email', models.CharField(blank=True, max_length=50, null=True, verbose_name='primary_email')),
                ('secondary_email', models.CharField(blank=True, max_length=50, null=True, verbose_name='secondary_email')),
                ('primary_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='primary_phone')),
                ('secondary_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='secondary_phone')),
                ('business_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='business_name')),
                ('address1', models.TextField(blank=True, null=True, verbose_name='address1')),
                ('address2', models.TextField(blank=True, null=True, verbose_name='address2')),
                ('city', models.IntegerField(blank=True, null=True, verbose_name='city')),
                ('province', models.IntegerField(blank=True, null=True, verbose_name='Province')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='country')),
                ('id_proof', models.FileField(upload_to='documents/')),
                ('is_approved', models.BooleanField(blank=True, null=True, verbose_name='is_approved')),
                ('is_lock', models.BooleanField(blank=True, null=True, verbose_name='is_lock')),
                ('allow_notifications', models.BooleanField(blank=True, null=True, verbose_name='allow_notifications')),
                ('fb_auth_token', models.TextField(blank=True, null=True, verbose_name='fb_auth_token')),
                ('created_by', models.IntegerField(blank=True, null=True, verbose_name='Created By')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created At')),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='Modified By')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='Modified At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_id', to='MakanakModels.Province'),
        ),
    ]
