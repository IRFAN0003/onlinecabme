from django.urls import path
from vehicle.views import UserVehicleTypeView

urlpatterns = [
    path('vehicle/',UserVehicleTypeView.as_view(),name='vehicle')
]