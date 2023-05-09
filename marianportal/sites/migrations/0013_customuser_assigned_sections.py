# Generated by Django 4.1.7 on 2023-05-05 01:16

from django.db import migrations
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0012_remove_customuser_assigned_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='assigned_sections',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Set', 'SET VALUE'), ('Grade 7 - Our Lady of Fatima', '7 - Our Lady of Fatima'), ('Grade 7 - Our Lady of Lourdes', '7 - Our Lady of Lourdes'), ('Grade 8 - Our Lady of the Pillar', '8 - Our Lady of the Pillar'), ('Grade 8 - Our Lady of the Penafrancia', '8 - Our Lady of Penafrancia'), ('Grade 9 - Our Lady of Loreto', '9 - Our Lady of Loreto'), ('Grade 9 - Our Lady of the Miraculous Medal', '9 - Our Lady of the Miraculous Medal'), ('Grade 10 - Our Lady of the Holy Rosary', '10 - Our Lady of the Holy Rosary'), ('Grade 10 - Our Lady of the Assumption', '10 - Our Lady of the Assumption'), ('Grade 11 - Our Lady of the COnsolacion', '11 - Our Lady of the Consolacion'), ('Grade 11 - Our Lady of Guadalupe', '11 - Our Lady of Guadalupe'), ('Grade 11 - Our Lady of the Candles', '11 - Our Lady of Candles'), ('Grade 12 - Our Lady of the Immaculate Conception', '12 - Our Lady of the Immaculate Conception'), ('Grade 12 - Our Lady of Mt. Carmel', '12 - Our Lady of Mt. Carmel'), ('Grade 12 - Our Lady of the Angels', '12 - Our Lady of the Angels')], max_length=506, null=True, validators=[multiselectfield.validators.MaxChoicesValidator(10)]),
        ),
    ]
