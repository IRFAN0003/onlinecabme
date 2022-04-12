from django.urls import path
from ride.views import UserRideView


urlpatterns = [
    
    path('home',UserRideView.as_view(),name='ride'),
]