# Generated by Django 5.0 on 2024-03-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0004_remove_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paths',
            name='Time',
            field=models.IntegerField(),
        ),
    ]
