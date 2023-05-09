# Generated by Django 4.1.7 on 2023-04-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that school ID already exists.'}, help_text='6 Digit School ID upon enrollment is required', max_length=10, unique=True, verbose_name='School ID'),
        ),
    ]
