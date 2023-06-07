# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:17:30 2023

@author: vamsh
"""

import os                # This is used for system function
import math          # The math library
import random     # For random numbers
import smtplib      # For email functions

num = "0123456789"
val = ""
for i in range(0,6):
    val+= num[math.floor(random.random()*10)]
OTP = val + " is your One-Time-Password for verification"
message = OTP

email = smtplib.SMTP('smtp.gmail.com', 587)  # To call the gmail account client
email.starttls()
email.login("vamshi.gajjela38507@gmail.com", "ixlsqabfljtubcyd")  # To login into your account successfully
id = input("Enter your email address : ")
email.sendmail('&&&&&&&&&&&',id,message)   # Sending the OTP email
x = input("Enter your One-Time-Password ~~> :  ")
if x == val :
    print("Hurray!! Your account has been successfully verified !! ")
else:
    print("Please carefully check your OTP once again !! ")

