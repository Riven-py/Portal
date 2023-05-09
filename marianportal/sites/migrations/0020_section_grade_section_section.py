# Generated by Django 4.1.7 on 2023-05-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0019_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='grade',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='section',
            field=models.CharField(default='Set', max_length=255),
        ),
    ]