# Generated by Django 5.0 on 2024-03-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0007_buses_columns_buses_rows_buses_spaceafter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stops',
            name='arrival_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='stops',
            name='departure_time',
            field=models.TimeField(null=True),
        ),
    ]
