# Generated by Django 4.2.3 on 2023-07-21 09:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SOVBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiv', models.BigIntegerField()),
                ('point_field', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('extra_data', models.JSONField(default=dict)),
            ],
        ),
    ]
