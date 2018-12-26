from django.shortcuts import render
from .models import Hobby
# Create your views here.


def index(request):
    #Home page
    hobbies=Hobby.objects.order_by()
    context={'hobbies':hobbies}
    return render(request,'index.html',context)

def about(request):
    #Page about author and contacts
    hobbies=Hobby.objects.order_by()
    context={'hobbies':hobbies}
    return render(request,'about.html',context)

def hobbies(request,hobby_id):
    hobby_name = Hobby.objects.get(id=hobby_id)
    hobbies=Hobby.objects.order_by()
    context={'hobbies':hobbies,'hobby_name':hobby_name}
    return render(request,'hobbies.html',context)