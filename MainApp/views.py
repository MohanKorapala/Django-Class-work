from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm
from .models import Entry, Topic
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
            new_topic = form.save()


            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request,'MainApp/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form':form,'topic':topic}
    return render(request,'MainApp/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('MainApp:topic',topic_id=topic.id)

    context = {'form':form,'topic':topic, 'entry':entry}
    return render(request,'MainApp/edit_entry.html', context)

