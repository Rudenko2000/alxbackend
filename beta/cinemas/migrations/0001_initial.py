# Generated by Django 4.0.3 on 2022-04-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seats', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('minimum_age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('publiszed', models.BooleanField()),
                ('tickets_availble', models.PositiveSmallIntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.movie')),
            ],
        ),
    ]