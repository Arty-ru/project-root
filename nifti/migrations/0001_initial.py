# Generated by Django 5.1.4 on 2024-12-19 20:24

import django.db.models.deletion
import nifti.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NiftiDir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(verbose_name='Директория')),
            ],
        ),
        migrations.CreateModel(
            name='NiftiStudyTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_type', models.CharField(default='Aneurysm', max_length=55, verbose_name='Тип исследования')),
            ],
        ),
        migrations.CreateModel(
            name='NiftiFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir', models.FileField(upload_to=nifti.models.content_file_name, verbose_name='Файл')),
                ('study_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nifti.niftidir', verbose_name='ID директории')),
            ],
        ),
        migrations.AddField(
            model_name='niftidir',
            name='study_type',
            field=models.ForeignKey(default=nifti.models.NiftiStudyTypes.get_default_pk, on_delete=django.db.models.deletion.PROTECT, to='nifti.niftistudytypes'),
        ),
    ]