# Generated by Django 5.1.4 on 2024-12-19 20:24

import dicom.models
import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DicomDirs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.TextField(verbose_name='Директория')),
                ('screens', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None, verbose_name='Снимки')),
            ],
        ),
        migrations.CreateModel(
            name='DicomStudyTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_type', models.CharField(default='Aneurysm', max_length=55, verbose_name='Тип исследования')),
            ],
        ),
        migrations.CreateModel(
            name='DicomFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir', models.FileField(upload_to=dicom.models.content_file_name, verbose_name='Файл')),
                ('study_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dicom.dicomdirs', verbose_name='ID директории')),
            ],
        ),
        migrations.AddField(
            model_name='dicomdirs',
            name='study_type',
            field=models.ForeignKey(default=dicom.models.DicomStudyTypes.get_default_pk, on_delete=django.db.models.deletion.PROTECT, to='dicom.dicomstudytypes'),
        ),
        migrations.CreateModel(
            name='DicomUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('dir', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dicom.dicomdirs', verbose_name='ID директории')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
        ),
    ]
