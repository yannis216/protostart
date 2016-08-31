from django.shortcuts import render
from .models import Event
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home/front_page.html', {})

def impressum(request):
    return render(request, 'home/impressum.html', {})

def datenschutz(request):
    return render(request, 'home/datenschutz.html', {})

def events(request):
    future_events= Event.objects.all().order_by('start_date')
    return render(request, 'home/events.html', {'future_events': future_events})
