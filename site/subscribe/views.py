from django.shortcuts import render
from myproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail , send_mass_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mass_mail(datatuple=(subject, message, EMAIL_HOST_USER,recepient))


        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})