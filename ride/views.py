from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView
from ride.form import UserDestinationForm
from ride.models import UserDestinationModel

class UserRideView(CreateView ):
    template_name = 'ride/ride.html'
    form_class = UserDestinationForm
    model = UserDestinationModel