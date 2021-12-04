# Generated by Django 3.2.6 on 2021-09-07 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oglas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=50)),
                ('tekst', models.TextField(blank=True)),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('vidljivost', models.CharField(choices=[('1', 'Korisnici'), ('2', 'Volonteri')], default='1', max_length=1)),
                ('za_brisanje', models.BooleanField(default=False)),
                ('arhiviran', models.BooleanField(default=False)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
