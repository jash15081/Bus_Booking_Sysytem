import re
import string
from django.core.mail import send_mail
from django.conf import settings
import random
def validate(username,password):
    pattern = "^[A-Za-z0-9_]*$"
    if(re.match(pattern,username)): 
        if(len(password) >= 8):
            return True
    return False

def sendotp(email):
    otp = ''.join(random.choice('0123456789') for _ in range(6))
    send_mail(
        subject='OTP for GoBus-Registration',
        message=f'Your OTP for Email verification of GoBus is :{otp}',
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    return otp