# Generated by Django 4.1.7 on 2023-05-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0021_remove_section_grade_remove_section_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='gr_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='sites.section'),
        ),
    ]