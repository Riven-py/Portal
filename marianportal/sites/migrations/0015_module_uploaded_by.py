# Generated by Django 4.1.7 on 2023-05-05 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0014_remove_module_uploaded_at_remove_module_uploaded_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]