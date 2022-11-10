from django.contrib.auth import views as auth_views
from event import views
from django.urls import include, path

app_name = "event"

urlpatterns = [
    path('registration', views.EventRegistrationView.as_view(),
        name='event-registration',
    ),
    path('list', views.EventListView.as_view(),
        name='event-list',
    ),
    path('reserve/<pk>', views.reserve,
        name='event-reserve'
    )
]