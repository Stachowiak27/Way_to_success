# Generated by Django 2.2.6 on 2019-10-13 13:52

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
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('type_tour', models.IntegerField(choices=[(1, 'pieszo'), (2, 'rowerem')])),
                ('difficulty', models.IntegerField(choices=[(1, 'Bardzo łatwa'), (2, 'Łatwa'), (3, 'Średnio trudna'), (4, 'Dla wytrwałych'), (5, 'Mega')])),
                ('distance', models.IntegerField(default=0)),
                ('time_tour', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(default='Wstaw opis')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail.Trail')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Wstaw swój komentarz')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail.Trail')),
            ],
        ),
    ]
