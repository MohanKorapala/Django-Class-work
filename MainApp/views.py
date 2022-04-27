from django.shortcuts import render, redirect

from MainApp.forms import TopicForm
from .models import Topic
from .forms import Topic

# Create your views here.

def index(request):
    return render(request,'MainApp/index.html')


def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics} #key(blue) is what is used in html flie the vlaue is what you use in the view file

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):#topic_id must be the same as teh urls.py file
    topic = Topic.objects.get(id=topic_id)# get and pass the id
    entries = topic.entry_set.order_by('-date_added')# descending order has the minus sign

    context = {'topic':topic,'entries':entries}# dictionary is used to pass objects from the view to the template in order for the template to have things 

    return render(request, 'MainApp/topic.html', context)# context is the dictionary

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_tpoic = form.save()


            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request,'MainApp/new_topic.html', context)


