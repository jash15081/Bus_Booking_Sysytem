from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('loginpage',views.login,name="loginpage"),
    path('signuppge',views.signup,name="signuppage"),
    path('otp',views.otp,name="otp"),
    path('logout',views.logout,name="logout"),
    path('findroutet',views.findroute,name="findroute"),
    path('showseats',views.showseats,name="showseats"),
    path('seatdetails',views.seatdetails,name="seatdetails"),
    path('booktickets',views.booktickets,name="booktickets"),
    path('cancelbooking',views.cancelbooking,name="cancelbooking"),
    path('showbookings',views.showbookings,name="showbookings"),
    path('getbus',views.getbus,name="getbus")
]