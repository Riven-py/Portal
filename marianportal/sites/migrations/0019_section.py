# Generated by Django 4.1.7 on 2023-05-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0018_subject_delete_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Set', max_length=255)),
            ],
        ),
    ]
