from django.contrib.auth import views as auth_views
from event import views
from django.urls import include, path

app_name = "event"

urlpatterns = [
    path('registration', views.EventRegistrationView.as_view(),
        name='event-registration',
    ),
]