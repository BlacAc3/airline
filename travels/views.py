from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    travels = Flight.objects.all()
    return render(request, "travels/index.html", {
        "travels": Flight.objects.all()
    })
    
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(travels=flight).all()
    return render(request, "travels/flight.html", {
        "flight": flight,
        "passengers":flight.passengers.all(),
        "non_passengers":non_passengers
    })
    
def book(request, flight_id):
    if request.method =="POST":
        flight = Flight.objects.get(pk= flight_id)
        passenger = Passenger.objects.get(pk=(int(request.POST["passenger"])))
        passenger.travels.add(flight)
        return HttpResponseRedirect (reverse("flight", args=(flight.id,)))