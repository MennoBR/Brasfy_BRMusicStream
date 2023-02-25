
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('home.html', views.home, name='home'),
]



