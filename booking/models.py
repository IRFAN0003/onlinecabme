from django.db import models
from booking.models import UserProfileModel
from booking.models import VehicleDetailsModel

class BookingModel(models.Model):
    user = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    booking_date = models.DateField()
    vehicle_type = models.ForeignKey(VehicleDetailsModel,on_delete=models.CASCADE)
    pick_up_detais= models.CharField(max_length=50)
    drowp_details = models.CharField(max_length=50)
    
    

