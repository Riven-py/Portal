# Generated by Django 4.1.7 on 2023-05-09 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0028_alter_module_subject_alter_subject_gr_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='grade_section',
        ),
    ]
