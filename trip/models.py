from django.db import models
from profiles.models import Driver, NormalUser
from vehicle.models import VehicleDetailsModel

class UserTripModel(models.Model):
    name = models.ForeignKey(Driver,on_delete=models.CASCADE)
    booking_date =models.DateTimeField(auto_now_add=True)
    cab_no= models.ForeignKey(VehicleDetailsModel,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class DriverTripModels(models.Model):
    name = models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    
    status = models.BooleanField(default=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name



