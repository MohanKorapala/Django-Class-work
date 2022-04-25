from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    return render(request,'MainApp/index.html')


def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics} #key(blue) is what is used in html flie the vlaue is what you use in the view file

    return render(request, 'MainApp/topics.html', context)