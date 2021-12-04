# Generated by Django 3.2.7 on 2021-10-02 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ankete', '0005_pitanja_tip_pitanja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitanja',
            name='anketa',
        ),
        migrations.AddField(
            model_name='anketa',
            name='pitanje',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stavka',
            name='pitanje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ankete.anketa'),
        ),
        migrations.DeleteModel(
            name='Otvorena_pitanja',
        ),
        migrations.DeleteModel(
            name='Pitanja',
        ),
    ]