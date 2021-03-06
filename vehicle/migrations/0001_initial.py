# Generated by Django 3.2.9 on 2022-04-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle_type', models.CharField(blank=True, choices=[('N', 'Normal'), ('S', 'Sedan'), ('Xl', 'Xl')], max_length=20, null=True)),
                ('status', models.BooleanField(default=True)),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
