#A form to submit inf. this case to submit a new topic 
from django import forms #
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic #The model we are gonna work with
		fields = ['text']#only text
		labels = {'text': ''}# to tell django no to add labels
		
		
class EntryForm(forms.ModelForm):
	class Meta:#A meta classs inside another class tell the class how to behave
		model= Entry
		fields= {'text'}# cuadro de texto
		labels= {'text': ' '}#sin etiquetas
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}#le da formato al cuadro de texto
