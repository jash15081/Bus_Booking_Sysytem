# Generated by Django 5.0 on 2024-03-14 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0003_remove_orders_location_remove_orders_route_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
    ]
