from django.contrib.auth import views as auth_views
from home import views
from django.urls import include, path

app_name = "home"

urlpatterns = [
    path('', views.IndexView.as_view(),
        name='home-index',
    ),
]