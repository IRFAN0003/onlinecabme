from django.forms import ModelForm
from vehicle.models import VehicleDetailsModel

class UserVehicleForm(ModelForm):
    class Meta:
        model = VehicleDetailsModel
        fields =['vehicle_no','vehicle_type']
    