# Generated by Django 5.0 on 2024-02-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.CharField(choices=[('bus_operator', 'bus_operator'), ('admin', 'admin'), ('normal', 'normal')], max_length=50),
        ),
    ]
