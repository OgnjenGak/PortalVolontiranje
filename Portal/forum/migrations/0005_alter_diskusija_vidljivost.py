# Generated by Django 3.2.4 on 2021-10-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210922_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diskusija',
            name='vidljivost',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Сви'), (2, 'Само логовани корисници')], default=1),
        ),
    ]