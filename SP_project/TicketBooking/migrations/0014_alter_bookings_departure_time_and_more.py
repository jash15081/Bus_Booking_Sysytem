# Generated by Django 5.0 on 2024-03-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0013_remove_bookings_date_remove_bookings_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='departure_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='reaching_time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]