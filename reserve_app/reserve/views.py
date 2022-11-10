from django.views import generic
from django.shortcuts import render
from reserve.models import Reservation

from PIL import Image
import qrcode
import base64
from io import BytesIO

class ReservationDetailView(generic.TemplateView):
    model = Reservation
    template_name = "reserve/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        uuid = Reservation.objects.filter(pk=self.kwargs['pk'])[0].token
        img = qrcode.make(uuid)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")

        context['qr'] = qr
        return context