from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/front_page.html', {})

def impressum(request):
    return render(request, 'home/impressum.html', {})

def datenschutz(request):
    return render(request, 'home/datenschutz.html', {})
