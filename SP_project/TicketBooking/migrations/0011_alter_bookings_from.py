# Generated by Django 5.0 on 2024-03-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0010_bookings_departure_time_bookings_reaching_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='From',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
