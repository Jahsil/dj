from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('', home, name = 'homepage'),
    path('other/', other, name = 'otherpage'),
    path('about/', about, name = 'about'),
]