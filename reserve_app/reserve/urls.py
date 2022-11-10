from django.contrib.auth import views as auth_views
from reserve import views
from django.urls import include, path

app_name = "reserve"

urlpatterns = [
    path('detail/<pk>', views.ReservationDetailView.as_view(),
        name='reserve-detail',
    ),
]