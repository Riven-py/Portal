# Generated by Django 4.1.7 on 2023-05-05 02:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0013_customuser_assigned_sections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='module',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='module',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='module',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='module',
            name='grade_section',
            field=models.CharField(max_length=255),
        ),
    ]
