from django.shortcuts import render, redirect
from django.http import HttpResponse

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
lightPin = 4
GPIO.setup(lightPin, GPIO.OUT)


def index(request):
    return render(request, "home.html")

def lightsOn(request):
    GPIO.output(lightPin, GPIO.HIGH)
    print('lights on')
    return redirect('/')
def lightsOff(request):
    GPIO.output(lightPin, GPIO.LOW)
    print('lights off')
    return redirect('/')