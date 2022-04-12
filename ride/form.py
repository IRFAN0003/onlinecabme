from django.forms import ModelForm
from ride.models import UserDestinationModel


class UserDestinationForm(ModelForm):
    class Meta:
        model  = UserDestinationModel
        exclude = ('create_on','status','update_on')