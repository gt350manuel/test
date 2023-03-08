"""Defines URL patterns for learning_logs."""

from django.urls import path

from .import views

app_name = 'learning_logs'
urlpatterns = [
	#HOME PAGE
	#this has three parameters the first, how it appears in the url
	#the sencod is the name of the function in the views file
	#the third is a a name we can used to link to the page insted of using the whole url

	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#we need to used the id of the topic for the individual topic template
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	]
