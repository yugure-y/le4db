from django.views import generic
from event.models import Event
from reserve.models import Reservation
from django.urls import reverse
from django.shortcuts import redirect
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

def reserve(request, pk):
    r = Reservation(user=request.user, event=Event.objects.filter(pk=pk)[0], accepted=False)
    r.save()
    return redirect('home:home-index')
