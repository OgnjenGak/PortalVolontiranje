# Generated by Django 3.2.7 on 2021-10-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankete', '0006_auto_20211002_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stavka',
            name='glasovi',
            field=models.PositiveSmallIntegerField(choices=[(1, 'У потпуности се не слажем.'), (2, 'Делимично се не слажем.'), (3, 'Нити се слажем, нити се не слажем.'), (4, 'Делимично се слажем.'), (5, 'У потпуности се слажем.'), (0, 'Не желим да одговорим.')], default=3),
        ),
    ]
