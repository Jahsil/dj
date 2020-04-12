from django.urls import path
from .views import *

app_name = "registration"
urlpatterns = [

    path('', regform , name = 'registration form'),
]
