# Generated by Django 4.1.7 on 2023-05-04 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0011_customuser_assigned_sections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='assigned_sections',
        ),
    ]
