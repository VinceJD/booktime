from django.http import HttpResponseRedirect
from django.shortcuts import render
from main import forms


# Create your views here.
def Home(request):
    return render(request, 'pages/home.html')


def About_us(request):
    return render(request, 'pages/aboutus.html')

def contact_us_view(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return HttpResponseRedirect('/')
    else:
        form = forms.ContactForm()

    context = { 'form' : form }
    return render(request, 'aboutus.html', context)

    