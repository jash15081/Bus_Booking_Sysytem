# Generated by Django 5.0 on 2024-03-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0017_alter_bookings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
