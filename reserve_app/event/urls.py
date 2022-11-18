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
    ),
    path('event-host-list', views.EventHostListView.as_view(),
        name='event-host-list',
    ),
    path('event-host-detail/<int:pk>', views.EventHostDetailView.as_view(),
        name='event-host-detail',
    ),
    path('event-host-update/<int:pk>', views.EventHostUpdateView.as_view(),
        name='event-host-update',
    ),
    path('event-host-delete/<int:pk>', views.EventHostDeleteView.as_view(),
        name='event-host-delete',
    ),
]