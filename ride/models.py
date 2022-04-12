from django.db import models

# Create your models here.

class UserDestinationModel(models.Model):
    
    Enter_pickup_location = models.CharField(max_length=100,blank=True,null=True)
    Enter_destination = models.CharField(max_length=100,blank=True,null=True)
    status = models.BooleanField(default=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return 
    