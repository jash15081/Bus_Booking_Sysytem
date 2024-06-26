# Generated by Django 5.0 on 2024-03-31 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0014_alter_bookings_departure_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='type',
        ),
        migrations.AddField(
            model_name='users',
            name='is_operator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seats',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TicketBooking.bookings'),
        ),
    ]
