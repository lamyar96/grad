from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Organization
from .models import Event
def Index(request):
    return HttpResponseRedirect(reverse('home_page'))
def home_page(request):
    return render(request,'app/home_page.html')
def list_followed_organizations(request):
    organizations = request.user.organization_set.all()  #user.org(indicates relation)
    return render(request,'app/list_org.html', {"orgnization": organizations})
def list_event(request):
    events=Event.objects.filter(organization__user=request.user)
    return render(request,'app/list_event',{'event':events})
def show_organization(request,ornization_id):
    orgnization=get_object_or_404(orgnization,pk=ornization_id)
    return render(request,'app/show.html',{'orgnization':orgnization})
def follow_organization(request,orgnization_id):
    request.method == "POST":
    fallow=orgnization_id.objects.create(request.user)
    return HttpResponseRedirect(reverse('list_event'))