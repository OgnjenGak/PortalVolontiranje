# Generated by Django 3.2.7 on 2021-09-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oglasi', '0019_alter_oglas_datum_isteka_oglasa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oglas',
            name='datum_isteka_oglasa',
        ),
    ]
