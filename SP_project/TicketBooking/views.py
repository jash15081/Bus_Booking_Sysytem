from django.shortcuts import render,get_object_or_404
from TicketBooking.models import Users
from TicketBooking.models import Locations
from TicketBooking.models import *
from funcs import loginfuncs
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.utils import timezone
# Create your views here.

        
def home(request):
    if 'islogged' in request.session and request.session['islogged'] == 'logged':
        user = Users.objects.get(username = request.session['username'])
        op = user.is_operator
        return render(request,'home.html',{'isoperator':op,'islogged':True,'name':request.session['name']})
    else:
        return render(request,'home.html')

def login(request):
    if request.method  == "POST":
        cusername = request.POST['username']
        cpassword = request.POST['password']

        if loginfuncs.validate(cusername,cpassword):
            try:
                exist = Users.objects.get(username = cusername,password = cpassword) 
            except Users.DoesNotExist:
                return render(request,'login.html',{'incorrect':True})
            request.session['name'] = exist.F_name
            request.session['islogged'] = 'logged'
            request.session['username'] = request.POST['username']
            request.session['email'] = exist.email
            return home(request)

        else:
            return render(request,'login.html',{'invalid':True})
            
    else:
        return render(request,'login.html')
def logout(request):
    del request.session['name']
    del request.session['islogged']
    del request.session['username']
    return home(request)
    
def signup(request):
        
    if(request.method == "POST"):

        cusername = request.POST['username']
        cpassword = request.POST['password']
        cemail = request.POST['email']
        cfname = request.POST['fname']
        clname = request.POST['lname']
        
        if(loginfuncs.validate(cusername,cpassword)):
                
                if Users.objects.filter(username = cusername).exists():
                    return render(request,'signup.html',{'uname_exist':True})
                elif Users.objects.filter(email = cemail).exists():
                    return render(request,'signup.html',{'email_exist':True})
                
                else:
                    request.session['email'] = cemail
                    request.session['username'] = cusername
                    request.session['password'] = cpassword
                    request.session['fname'] = cfname
                    request.session['lname'] = clname
                    return otp(request)
        else:
            return render(request,'signup.html',{'invalid':True})

       

    return render(request,'signup.html')

def otp(request):

    if(request.method == "GET"):
        if request.GET['btn'] == "Verify OTP":
            if request.GET['otp'] == request.session['otpp']:
                usr = Users(username=request.session['username'],
                            password = request.session['password'],
                            email = request.session['email'],
                            F_name = request.session['fname'],
                            L_name = request.session['lname'],
                            )
                Users.save(usr)
                del request.session['username'],
                del request.session['password'],
                del request.session['email'],
                del request.session['fname'],
                del request.session['lname'],
                return render(request,'login.html')
            else:
                return render(request,'otp.html',{'incorrect':True})
        else:
            request.session['otpp'] = loginfuncs.sendotp(request.session['email'])
            return render(request,'otp.html')
    else:
        request.session['otpp'] = loginfuncs.sendotp(request.session['email'])
        return render(request,'otp.html')



def findroute(request):
    locs = Locations.objects.all()
    if request.method == "POST":
        loc_from = request.POST['from']
        loc_to = request.POST['to']
        request.session['loc_from'] = loc_from
        request.session['loc_to'] = loc_to
        request.session['rdate'] = request.POST['date']
        return showroutes(request)
    else:
        return render(request,'findroute2.html',{'locs':locs})

def showroutes(request):
    loc_from = request.session['loc_from']
    loc_to = request.session['loc_to']
    rdate = request.session['rdate']
    edges = stops.objects.filter(path__From__fullName = loc_from,Route__date = rdate)
    c_list= []
    class details:
        def __init__(self,distance,route,departure_time,arrival_time):
            self.distance = distance
            self.route = route
            self.arrival_time = arrival_time
            self.departure_time = departure_time
    for option in edges:
        fareperkm = 3
        if option.Route.Bus.bus_class == 'AC-sleeper':
            fareperkm = 5
        elif option.Route.Bus.bus_class == 'AC-sitting':
            fareperkm = 4
        elif option.Route.Bus.bus_class == 'Luxury-sitting':
            fareperkm = 3
        elif option.Route.Bus.bus_class == 'Luxury-sleeper':
            fareperkm = 3.5
        elif option.Route.Bus.bus_class == 'Express':
            fareperkm = 2.5
        elif option.Route.Bus.bus_class == 'Mini-Bus':
            fareperkm = 2
        loc = option.path.To
        distance = option.path.Distance
        if(loc.fullName == loc_to):
            d1 = details(distance,option.Route,option.departure_time,option.arrival_time)
            c_list.append(d1)
        while stops.objects.filter(path__From = loc,Route = option.Route).exists():
            stop = stops.objects.get(path__From = loc,Route = option.Route)
            loc = stop.path.To
            distance += stop.path.Distance 
            if loc.fullName == loc_to:
                d1 = details(round(distance*fareperkm,2),option.Route,option.departure_time,stop.arrival_time)
                c_list.append(d1)
                break;

   
    if(not len(c_list)):
            return render(request,'showroutes2.html',{'no_routes':True})
    return render(request,'showroutes2.html',{'details':c_list})

def showseats(request):
    if request.method == "POST":
        price = request.POST['price']
        request.session['price'] = price
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']
        request.session['arrival_time'] = arrival_time
        request.session['departure_time'] = departure_time
        route_id = request.POST['route']
        request.session['route_id'] = route_id
        route = Routes.objects.get(pk = route_id)
        print(route)
        bus = route.Bus
        seats = Seats.objects.filter(bus = bus)
        remaining = bus.columns - bus.spaceAfter + 1
        return render(request,'showseats.html',{'space':2,'route':route,'bus':bus,'seats':seats,'price':price,'rows':bus.rows,'columns':bus.columns,'remaining':remaining,'arrival_time':arrival_time,'departure_time':departure_time})
    return render(request,'showseats.html')

def seatdetails(request):
    if request.method == "POST":
        seats = request.POST.getlist('selected_seats')
        request.session['seats'] = seats
        route_id = request.session['route_id']
        route = Routes.objects.get(pk = route_id)
        price = request.session['price']
        total_price = float(price) * len(seats)
        request.session['total_amount'] = total_price
    return render(request,'getseatdetails.html',{'seats':seats,'amount':total_price,'route':route})

def booktickets(request):
    if request.method == "POST":
        seats = request.session['seats']
        route_id = request.session['route_id']
        route = Routes.objects.get(pk = route_id)
        no_plate  = route.Bus.number_plate
        user = Users.objects.get(username = request.session['username'])
        From = request.session['loc_from']
        To = request.session['loc_to']
        departure_time = request.session['departure_time']
        reaching_time = request.session['arrival_time']
        amount = request.session['total_amount']
        b = Bookings(route = route,user = user,From = From,To =To,departure_time = departure_time , reaching_time = reaching_time,Amount = amount)
        Bookings.save(b)
        msg = "From: "+From+"   \nTo:"+To+" \nDeparture Time:" +departure_time+   "\nReaching Time: "+reaching_time+"\nAmount: "+str(amount)+"  \nBooking Id: "+str(b.id)+"\n Number Plate : "+no_plate+"  \nSeat No: "
        for s in seats:
            str_passenger = "passenger_"+s
            str_type = "type_"+s
            passenger = request.POST[str_passenger]
            type = request.POST[str_type]
            bus = route.Bus
            seat = Seats.objects.get(bus = bus,seat_no = s)
            seat.name = passenger
            seat.type = type
            seat.is_Booked = True
            seat.booking = b
            Seats.save(seat)
            msg = msg+str(seat.seat_no)+",  "
        send_mail(
        subject = 'Tickets for GoBus Reservation',
        message = msg
         ,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[request.session['email']]
        )
        return render(request,'ticket_booked.html')
    return render(request,'ticket_booked.html')
        
def cancelbooking(request):
    booking_id = request.POST['booking']
    booking = Bookings.objects.get(pk = booking_id)
    bus = booking.route.Bus
    seats = Seats.objects.filter(bus = bus,booking = booking)
    for s in seats:
        s.is_Booked = False
        s.booking = None
        s.name = None
        s.type = "normal"
        Seats.save(s)
    msg = "Your Ticket has been cancelled successfully !! \nFrom: "+booking.From+"   \nTo:"+booking.To+"    \nAmount: "+str(booking.Amount)+"  \nBooking Id: "+str(booking.id)
    for s in seats:
        msg = msg+" "+str(s.seat_no)
    send_mail(
    subject = 'Cancellation of Tickets for GoBus n',
    message = msg
        ,
    from_email = settings.EMAIL_HOST_USER,
    recipient_list=[request.session['email']]
    )
    Bookings.delete(booking)
    return render(request,'cancelbooking.html')

def showbookings(request):
    user = Users.objects.get(username = request.session['username'])
    bookings = Bookings.objects.filter(user = user)
    return render(request,'showbookings.html',{'bookings':bookings})

def getbus(request):
    if request.method == 'POST':
        number_plate = request.POST['numberplate']
        bus = Buses.objects.get(number_plate = number_plate)
        seats = Seats.objects.filter(bus = bus,is_Booked = True)
        return render(request,'showpassenger.html',{'seats':seats,'bus':bus})
    return render(request,'getbus.html')
