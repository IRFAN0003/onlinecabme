from django.db import models

class VehicleDetailsModel(models.Model):
    CHOICES_VEHICLE_MODEL = [
            ('Normal','Normal'),
            ('Sedan','Sedan'),
            ('Xl','Xl')
    ]
    vehicle_owner_name = models.CharField(max_length=20,blank=True,null=True)
    vehicle_no = models.CharField(max_length=20,blank=True,null=True)
    vehicle_type = models.CharField(choices=CHOICES_VEHICLE_MODEL ,max_length=20,blank=True,null=True) 
    status = models.BooleanField(default=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.vehicle_no
  

    
    


