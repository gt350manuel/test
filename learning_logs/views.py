from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required # For restricting 
from django.http import Http404

#Create your views here.
"""
#Nota: Templates are store in a folder called learning_logs inside a templatefolder
#inside the learning_logs principal folder."""

def index(request):
	"""The home page for Learning Log."""
	return render(request, 'learning_logs/index.html') 

@login_required 
#its a decorator, restrict access to the requested Page if the user is not authenticated.
#has to add a the following line: LOGIN_URL = 'users:login' to project settings at the end
def topics(request):
	"""Show all topics"""
	topics= Topic.objects.filter(owner=request.user).order_by('date_added')
	"""
		# will filter only the topics associeted with that user.
		#this part is when we are conecting topics with users 
		#topics = Topic.objects.order_by('date_added')#get the Topics from de data base
		"""
	context = {'topics': topics}#create a list with the topics will be sent to the template
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id): #topic_id saves de parameter the url is sending
	"""Show a single topic an all its entries."""
	topic = Topic.objects.get(id=topic_id) #we use get to retrive the topic, base in its id
	#MAKE SURE THE TOPIC BELONGS TO THE CURRENT USER:
	check_topic_owner(request, topic)
	#if topic.owner != request.user:
	#	raise Http404 
	"""
	#even though the user is not authenticated or is a diferent user, it is still posible to see pages just by coping the Url to
	#the broswer, this code avoids that."""
	entries = topic.entry_set.order_by('-date_added') 
	"""
	#the - display the most recent entries first
    #this last too lines are called queries, because they query the data base for specif inf.	"""
	context = {'topic': topic, 'entries': entries}#save the data in a dic, to be send to the topic template
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic"""
	if request.method != 'POST': #whether the request is a GET or POST
		#No data submitted; create a blanck form. b
		form= TopicForm()
	else:
		#POST data submitted, process data.
		form = TopicForm(data=request.POST)#
		if form.is_valid():
			#form.save()
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			"""
			#before adding these 3 last lines of code, an error ocurred, 'IntegrityError along with NOT NULL
            #constraint failed: learning_logs_topic.owner_id.' this was because the topic was not associetted correctly with a its user.
            #To correctly associate a user with its topics, first neeed to add the Forei gnKey method at topic model, so m  nodels can be conected,
            #then in the view funtion, using the las 3 lines of codes you associate the topic with the correct user. """
			return redirect('learning_logs:topics')#Redirects the user to a view funtion
			 
	#DISPLAY A BLANK OR INDIVIDUAL FORM
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)
	"""
	#GET AND POST: GET is used to get data from the server, POST when user needs to submitt inf through a form.
	#Initially when the page is requested the broswer will send a GET request because somethimes user is asking for a 
	#form filled of inf. from the server, in this case it´s not necesary just need a empty form to fill and then submitt
	#inf, using the POST request to send data to the server"""
	
@login_required  
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic"""
	topic= Topic.objects.get(id=topic_id)
	check_topic_owner(request, topic)
	"""
	#if topic.owner != request.user:
		#raise Http404
	    #even though the user is not authenticated or is a diferent user, it is still posible to see pages just by coping the Url to
		#the broswer, this code avoids that."""
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = EntryForm()
	else:
		#POST data submitted; process data.
		form = EntryForm(data=request.POST)#creating an instance of EntryForm
		if form.is_valid():# validating data
			new_entry = form.save(commit=False)#save the form with the new data in an object, and tells djangon not to save to database yet
			new_entry.topic= topic #relate to the topic
			new_entry.save()# save to data base
			return redirect('learning_logs:topic', topic_id=topic_id)
	
	#Display a blank or invalid form.
	context = {'topic': topic, 'form': form}#this part will ejecute with a black form of invalid data form 
	return render (request, 'learning_logs/new_entry.html', context)
	
@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry"""
	entry = Entry.objects.get(id=entry_id)#get the entry using the entry_id send by the url
	topic =entry.topic #get the topic that is alredy related to entry
	check_topic_owner(request, topic)
	if request.method != 'POST': #the user is requesting a form fill with the entry inf, so can be editted and saved
		#Initial reques; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		#Post data submitted, proces data.
		#the entry has been editten and user request to update the entry
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():#validate the edited entry
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)#redirect to topic view
		
	context = {'entry': entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)
	
	

def check_topic_owner(request, topic):
	""""check if the topic owner maches the current user"""
	if topic.owner != request.user:
		raise Http404
	

	
	
	
	
	
	
	
	
	
	
	
