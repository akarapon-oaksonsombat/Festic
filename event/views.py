from django.db.models.fields.related import ForeignKey
from django.shortcuts import render
from .models import EventDetail, Participant
# Create your views here.
def home(request):
    context = {
        'title':'Home',
        }
    return render(request, 'home.html', context)
def detail(request, event_id):
    event = EventDetail.objects.get(id=event_id)
    list =  Participant.objects.all().filter(event_id=event_id)
    context = {
        'title': 'Detail', 
        'event': event,
        'list': list
        }
    return render(request, 'detail.html', context)
def all(request):
    list = EventDetail.objects.order_by('id')
    context = {
        'title': 'Detail', 
        'list': list
        }
    return render(request, 'all.html', context)