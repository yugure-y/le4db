from django import forms
from reserve.models import Reservation

class AcceptForm(forms.Form):
    token = forms.CharField(
        max_length=100
    )