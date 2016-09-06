from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt



# Create your views here.
@xframe_options_exempt
def home(request):
    return render(request, 'home/front_page.html', {})

def impressum(request):
    return render(request, 'home/impressum.html', {})

def datenschutz(request):
    return render(request, 'home/datenschutz.html', {})
