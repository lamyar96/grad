from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Organization
from .models import Event

def list_organization(request,organization_id):
    organization=get_object_or_404(Organization,pk=organization_id)
    return render(request,'app/list_org.html')
def list_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id)
def show_organization(request):
    orgnization=Organization.objects.all()
    return render(request,'app/show.html')
