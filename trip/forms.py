from django.forms import ModelForm
from trip.models import UserTripModel


class TripForm(ModelForm):
    class Meta:
        model  = UserTripModel
        exclude = ('status','create_on','update_on',)