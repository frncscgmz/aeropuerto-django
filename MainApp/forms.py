from django import forms
from Aeropuerto.MainApp.models import Destinos

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label='Correo electronico.')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self): #La funcion empieza con clean_ y despues el nombre del metodo que buscar al activarse
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Faltan palabras!")
		return message


