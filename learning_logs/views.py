from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages import add_message
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	"""Homepage for Learning Log."""
	return render(request, "learning_logs/index.html")

@login_required
def topics(request):
	"""Show all topics.
	
	We first import the model associated with the data we need. The topics() function needs one parameter: the request object Django received from the server. At w we query the database by asking for the Topic objects, sorted by the date_added attribute. We store the resulting queryset in topics. 
	
	We define a context that we’ll send to the template. A context is a dictionary in which the keys are names we’ll use in the template to access the data and the values are the data we need to send to the template. In this case, there’s one key-value pair, which contains the set of topics we’ll display on the page. When building a page that uses data, we pass the context variable to render() as well as the request object and the path to the template.
	"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request, "learning_logs/topics.html", context)

@login_required
def topic(request, topic_id):
	"""Show a single topic result and all its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added') # The minus sign sorts in reverse order. The most recent entry first. 
	reverse('learning_logs:topic', args=[topic_id])
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic1.html', context)

@login_required
def new_topic(request):
	"""Add new topic."""
	if request.method != 'POST':
		form = TopicForm()
		
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
		else:
			add_message(request, messages.ERROR, 'Submission failed.\
			   Check your connection and try again')
		
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required	
def new_entry(request, topic_id):
	"""Add new entry."""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic'),
						args=[topic_id])
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required	
def edit_entry(request, entry_id):
	"""Edit entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if request.method != 'POST':
		#Initial request. Pre-fill form with info from existing entry object
		form = EntryForm(instance=entry)
	else:
		"""
		When processing a POST request, we pass the instance=entry argument
and the data=request.POST argument to tell Django to create a form
instance based on the information associated with the existing entry object,
updated with any relevant data from request.POST.
		"""
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic'),
				   args=[topic.id])
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
		