from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    front_events=Event.objects.filter(end_date__gte=datetime.date.today()).order_by('start_date')
    return render(request, 'home/front_page.html', {'front_events': front_events})

def impressum(request):
    return render(request, 'home/impressum.html', {})

def datenschutz(request):
    return render(request, 'home/datenschutz.html', {})

def events(request):
    future_events= Event.objects.filter(end_date__gte=datetime.date.today()).order_by('start_date')
    past_events=Event.objects.filter(end_date__lte=datetime.date.today()).order_by('start_date')
    return render(request, 'home/events.html', {'future_events': future_events, 'past_events': past_events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'home/event_detail.html', {'event': event})
