# Generated by Django 2.2.6 on 2019-10-05 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigParking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Big_Parking',
                'verbose_name_plural': 'Big_Parkings',
            },
        ),
        migrations.CreateModel(
            name='Parkomat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('work_time', models.CharField(max_length=255)),
                ('big_parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_parking', to='main.BigParking')),
            ],
            options={
                'verbose_name': 'Parking',
                'verbose_name_plural': 'Parkings',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_count', models.TimeField(auto_now_add=True)),
                ('state_number', models.CharField(max_length=255)),
                ('parking_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_place', to='main.Parkomat')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
