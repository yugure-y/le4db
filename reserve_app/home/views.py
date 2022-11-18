from django.views import generic
from django.shortcuts import render
from reserve.models import Reservation

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['reservations'] = Reservation.objects.filter(user=user)
        return context