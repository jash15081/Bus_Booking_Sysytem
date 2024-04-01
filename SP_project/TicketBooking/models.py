from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid

class Users(models.Model):
   
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 30)
    F_name = models.CharField(max_length = 50)
    L_name = models.CharField(max_length = 50)
    is_operator = models.BooleanField(default = False)
    def __str__(self):
        return self.username

class Agencies(models.Model):
    Agency_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.Agency_name

class Buses(models.Model):
    CLASSES = (
        ('AC-sitting','AC-sitting'),
        ('AC-sleeper','AC-sleeper'),
        ('Luxury-sitting','Luxury-sitting'),
        ('Luxury-sleeper','Luxury-sleeper'),
        ('Express','Express'),
        ('Mini-Bus','Mini-Bus')

    )
    number_plate = models.CharField(max_length = 15)
    capacity = models.IntegerField(max_length = 100)
    bus_class = models.CharField(max_length = 30,choices = CLASSES)
    name =  models.CharField(max_length = 50)
    Company =  models.CharField(max_length = 15)
    columns = models.IntegerField(max_length = 20,null = True,blank = True)
    spaceAfter = models.IntegerField(max_length = 20,null = True,blank = True)
    rows = models.IntegerField(max_length = 50,null = True,blank = True)
    Agency = models.ForeignKey(Agencies, null = True,on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Locations(models.Model):
    fullName = models.CharField(max_length = 50)
    shortName = models.CharField(max_length = 50)
    def __str__(self) -> str:
        return self.fullName

class Paths(models.Model):
    From = models.ForeignKey(Locations,related_name = 'source',null = False,on_delete = models.CASCADE)
    To = models.ForeignKey(Locations,related_name = 'destination',null = False,on_delete = models.CASCADE)
    Distance = models.FloatField()
    Time  = models.IntegerField()
    def __str__(self):
        return self.From.fullName +" - "+ self.To.fullName

class Routes(models.Model):
    Bus = models.ForeignKey(Buses,null = True,on_delete = models.SET_NULL)
    Departure_loc = models.ForeignKey(Locations,related_name = 'departure',null = False,on_delete = models.CASCADE)
    Arrival_loc = models.ForeignKey(Locations,related_name = 'arrival',null = False,on_delete = models.CASCADE)
    Price = models.FloatField()
    Distance = models.FloatField()
    Stops = models.ManyToManyField(Paths,through='stops')
    date = models.DateField()
    def __str__(self):
        return self.Departure_loc.fullName + " - " + self.Arrival_loc.fullName

class stops(models.Model):
    Route = models.ForeignKey(Routes,null = False,on_delete = models.CASCADE)
    path = models.ForeignKey(Paths,null = False,on_delete = models.CASCADE)
    order = models.IntegerField()
    arrival_time = models.TimeField(null=True)
    departure_time = models.TimeField(null=True)
    def __str__(self):
        return self.path.From.fullName + " - " + self.path.To.fullName
    
import random
import string

def generate_random_id():
    while True:
        characters = string.ascii_letters + string.digits
        new_id = ''.join(random.choice(characters) for _ in range(10))
        if not Bookings.objects.filter(id=new_id).exists():
            return new_id
class Bookings(models.Model):
    id = models.CharField(max_length = 15,primary_key  =True , default = generate_random_id,editable = False)
    route = models.ForeignKey(Routes,null = False,on_delete = models.CASCADE)
    user = models.ForeignKey(Users,null = False,on_delete = models.CASCADE)
    From = models.CharField(null = True,max_length = 20)
    To = models.CharField(null = True,max_length = 20)
    departure_time = models.CharField(max_length = 20,null = True)
    reaching_time = models.CharField(max_length = 20,null = True)
    
    Amount = models.DecimalField(null = False,max_digits = 10,decimal_places = 2)
    def __str__(self):
        return self.user.F_name+ " : " + self.From
    


class Seats(models.Model):
    '''Types = ('normal' , 'woman' , 'child' , 'handicap' , 'elder-citizen')'''
    Types = (
        ('normal','normal'),
        ('woman','woman'),

    )
    seat_no = models.IntegerField(max_length= 100 )
    is_Booked = models.BooleanField()
    name = models.CharField(max_length = 50,null = True,blank = True)    
    booking = models.ForeignKey(Bookings,null = True,blank = True,on_delete = models.SET_NULL)
    bus = models.ForeignKey(Buses,null = False,on_delete = models.CASCADE)
    type = models.CharField(max_length = 30,choices = Types)
    def __str__(self):
        return self.bus.name + " : "+str(self.seat_no)

