from django.shortcuts import render
from django.views.generic import TemplateView


class UserVehicleTypeView(TemplateView):
    template_name = 'vehicle/vehicle_type.html'


