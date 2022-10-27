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

class EventListView(generic.ListView):
    model = Event
    template_name = "event/list.html"

    def get_queryset(self):
        return Event.objects.order_by('date')