from django.views import generic
from django.shortcuts import render, redirect
from reserve.models import Reservation
from reserve.forms import AcceptForm

from PIL import Image
import qrcode
import base64
from io import BytesIO

from django.contrib import messages
from django.core import exceptions

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

class AcceptView(generic.FormView):
    model = Reservation
    template_name = 'reserve/accept.html'
    raise_exception = True
    form_class = AcceptForm

    def form_valid(self, form):
        token = form.cleaned_data['token']
        try:
            event = Reservation.objects.get(token=token)
        except exceptions.ObjectDoesNotExist:
            return self.form_invalid(form)
        event.accepted = True
        event.save()
        messages.info(self.request, "受付に成功しました。")
        return redirect('reserve:accept')

    def form_invalid(self, form):
        messages.error(self.request, "不正なQRコードです。")
        return super().form_invalid(form)
