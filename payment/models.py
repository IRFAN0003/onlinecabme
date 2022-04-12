from django.db import models
# from profiles.models import UserProfileModel


class PaymentModel(models.Model):
    # user = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    # booking = models.ForeignKey(,on_delete=models.SET_NULL,blank=True,null=True)
    status = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    receipt = models.CharField(max_length=20)
    description = models.CharField(max_length=100,blank=True,null=True)