from django.shortcuts import render
from .models import Hobby,Activity,Event
# Create your views here.


def index(request):
    #Home page
    hobbies=Hobby.objects.order_by('text')
    context={'hobbies':hobbies}
    return render(request,'index.html',context)

def about(request):
    #Page about author and contacts
    hobbies=Hobby.objects.order_by('text')
    context={'hobbies':hobbies}
    return render(request,'about.html',context)

def hobbies(request,hobby_id):
    #Page about my hobbies
    hobby_name = Hobby.objects.get(id=hobby_id)
    hobbies=Hobby.objects.order_by('text')
    activities=hobby_name.activity_set.order_by('text')
    context={'hobbies':hobbies,'hobby_name':hobby_name,'activities':activities}
    return render(request,'hobbies.html',context)

def activities(request,hobby_id,activity_id):
    # Page about my activities in some hobby
    hobby_name = Hobby.objects.get(id=hobby_id)
    hobbies = Hobby.objects.order_by('text')
    activity_name = hobby_name.activity_set.get(id=activity_id)
    events=activity_name.event_set.order_by('-date')
    context={'hobbies':hobbies,'hobby_name':hobby_name,'activity_name':activity_name,'events':events}
    return render(request, 'activities.html', context)