from django.shortcuts import render, redirect
from django.contrib.auth import login#to log the user if registration is correct 
from django.contrib.auth.forms import UserCreationForm# default form to register a user

# Create your views here.
def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		#Display blank registration form.
		form = UserCreationForm()
	else:
		#Proces completed form.
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#Log the user in an then redirect to home page.
			login(request, new_user)
			return redirect('learning_logs:index')
			
	#Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register.html', context)		
 
