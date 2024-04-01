from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Buses,Seats

@receiver(post_save, sender=Buses)
def create_seats(sender, instance, created, **kwargs):
    if created:
        
        num_seats = instance.capacity  

        
        for i in range(1, num_seats + 1):
            Seats.objects.create(bus=instance, seat_no=i,is_Booked = False)