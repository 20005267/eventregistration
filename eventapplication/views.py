from django.shortcuts import render
from .models import Participant
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.Name = request.POST.get('Name','-')
        p1.Email = request.POST.get('Email','-')
        p1.phone = request.POST.get('phone','000')
        p1.Place = request.POST.get('Place','-')
    
        if len(Participant.objects.all()) > 15:
            return render(request, 'eventapplication/failed.html', context)
        else:
            p1.save()
            return render(request, 'eventapplication/success.html', context)
    if request.method == 'GET':
        context['name'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['place'] = ''
    return render(request, 'eventapplication/register.html', context)

def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)

def failed(request):
    context = {}
    return render(request, 'eventapplication/failed.html', context)

def participants(request):
    context = {}
    context['participants'] = Participant.objects.all()
    return render(request, 'eventapplication/participants.html', context)