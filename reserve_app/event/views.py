from django.views import generic
from event.models import Event
from django.urls import reverse
from event.forms import EventRegistrationForm

# Create your views here.
class EventRegistrationView(generic.CreateView):
    model = Event
    template_name = "event/registration.html"
    form_class = EventRegistrationForm

    def get_success_url(self):
        return reverse('home:home-index')