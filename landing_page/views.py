from django.shortcuts import render
from .models import Picture




def home(request):
    return render(request, 'landing_page/home.html')

def about(request):
    return render(request, 'landing_page/about.html')

def gallery(request):
    pictures = Picture.objects.all()
    context = {'pictures': pictures}
    return render(request, 'landing_page/gallery.html', context)

def contact(request):
    return render(request, 'landing_page/contact.html')