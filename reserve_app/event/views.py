from django.views import generic
from event.models import Event
from reserve.models import Reservation
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from event.forms import EventRegistrationForm, EventUpdateForm

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

class EventHostListView(generic.ListView):
    model = Event
    template_name = "event/host_list.html"

    def get_queryset(self):
        return Event.objects.order_by('date')

class EventHostDetailView(generic.DetailView):
    model = Event
    template_name = "event/host_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['count'] = Reservation.objects.filter(event=id).count()
        context['accepted_count'] = Reservation.objects.filter(event=id, accepted=True).count()
        context['reserved'] = Reservation.objects.filter(event=id)
        context['staff'] = Reservation.objects.filter(event=id)
        return context

class EventHostUpdateView(generic.UpdateView):
    model = Event
    template_name = "event/host_update.html"
    form_class = EventUpdateForm

    def get_success_url(self):
        return reverse('event:event-host-list')

class EventHostDeleteView(generic.DeleteView):
    model = Event
    template_name = "event/host_delete.html"
    success_url = reverse_lazy('event:event-host-list')
    