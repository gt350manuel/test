from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic (models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	"""
	#create a foreign Key relationship to the user model.
	   #if the user is deleted all topics associated with that user will be delated as well.
	   #with the Foreing key relation ship and the code in the view model, the topics will be from now on associated with the user that create it
	   #topics created before that did´t hava that connection so there is a way to associate them to an user as well as the super user. look for inf page 594
	   #when we migrate, will tell python to manage to modify the database structure, but we can delete all using 'python manage.py flush'
	   #when a user is delated all the structure and inf associated will be delated as well."""
	def __str__(self):
		"""Return a string representation of the model"""
		return self.text 
	
class Entry(models.Model):
	"""Something specific learned about a topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#ForeingKey is a data base term, conects each entry to an specific term.
	text = models.TextField()                                 #on_deleta=models.Cascada, when a topic is delated all entries as well 
	date_added = models.DateTimeField(auto_now_add= True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""Return a string representation of the model."""
		return f"{self.text[:50]}..."
 
 
