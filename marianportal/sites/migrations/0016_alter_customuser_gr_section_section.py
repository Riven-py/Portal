# Generated by Django 4.1.7 on 2023-05-08 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0015_module_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gr_section',
            field=models.CharField(choices=[('Set', 'SET VALUE'), ('Grade 7 - Our Lady of Fatima', '7 - Our Lady of Fatima'), ('Grade 7 - Our Lady of Lourdes', '7 - Our Lady of Lourdes'), ('Grade 8 - Our Lady of the Pillar', '8 - Our Lady of the Pillar'), ('Grade 8 - Our Lady of the Penafrancia', '8 - Our Lady of Penafrancia'), ('Grade 9 - Our Lady of Loreto', '9 - Our Lady of Loreto'), ('Grade 9 - Our Lady of the Miraculous Medal', '9 - Our Lady of the Miraculous Medal'), ('Grade 10 - Our Lady of the Holy Rosary', '10 - Our Lady of the Holy Rosary'), ('Grade 10 - Our Lady of the Assumption', '10 - Our Lady of the Assumption'), ('Grade 11 - Our Lady of the COnsolacion', '11 - Our Lady of the Consolacion'), ('Grade 11 - Our Lady of Guadalupe', '11 - Our Lady of Guadalupe'), ('Grade 11 - Our Lady of the Candles', '11 - Our Lady of Candles'), ('Grade 12 - Our Lady of the Immaculate Conception', '12 - Our Lady of the Immaculate Conception'), ('Grade 12 - Our Lady of Mt. Carmel', '12 - Our Lady of Mt. Carmel'), ('Grade 12 - Our Lady of the Angels', '12 - Our Lady of the Angels')], default='Set', max_length=255),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', multiselectfield.db.fields.MultiSelectField(choices=[('GenChem1', 'General Chemistry 1'), ('GenPhy1', 'General Physics 1'), ('Entrep', 'Entrepeneurship'), ('MIL', 'Media Information Literacy'), ('Philo', 'Philosophy')], max_length=33, validators=[multiselectfield.validators.MaxChoicesValidator(10)])),
                ('section_name', models.ForeignKey(default='Section', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Grade and Section')),
            ],
        ),
    ]
