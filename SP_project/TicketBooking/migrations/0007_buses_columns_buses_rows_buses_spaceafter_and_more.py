# Generated by Django 5.0 on 2024-03-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketBooking', '0006_alter_seats_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='columns',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='buses',
            name='rows',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='buses',
            name='spaceAfter',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seats',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
