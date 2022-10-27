from django import forms
from event.models import Event

class EventRegistrationForm(forms.ModelForm):
    class Meta(object):
        model = Event
        fields = (
            'title', 'date', 'place', 'capacity'
        )