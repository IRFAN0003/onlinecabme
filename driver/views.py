from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

class DriverDashboardView(TemplateView):
    template_name = 'driver/dashboard.html'

    