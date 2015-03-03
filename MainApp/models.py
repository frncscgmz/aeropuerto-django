from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserCreationFormExtended(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationFormExtended, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['username'].label = 'Usuario'
		self.fields['first_name'].label = 'Nombre'
		self.fields['last_name'].label = 'Apellido'
		self.fields['email'].label = 'Email'
		self.fields['password1'].label = 'Clave'
		self.fields['password2'].label = 'Repetir Clave'

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email',)

class ReservacionManager(models.Manager):
	def boleto_count(self,keyword):
		return self.filter(destino__icontains=keyword).count()

class Destinos(models.Model):
	nombre=models.CharField(max_length=30,null=False)
	origen=models.CharField(max_length=30)
	destino=models.CharField(max_length=30)
	fecha_partida=models.DateField(blank=False)
	fecha_llegada=models.DateField(blank=False)
	objects = ReservacionManager()

	def __str__(self):
		return '%s %s %s %s %s'%(self.nombre,self.origen,self.destino,self.fecha_partida,self.fecha_llegada)

	class Admin():
		pass

class Reservacion(models.Model):
	destino=models.ForeignKey(Destinos)
	boletos=models.IntegerField()
	primeraclase=models.BooleanField()
	usuario=models.ForeignKey(User) 

	def __str__(self):
		return '%s %s %s %s'%(self.destino,self.boletos,self.primeraclase,self.usuario)

	class Admin():
		pass

class ReservationForm(ModelForm):
	class Meta:
		model = Reservacion
		#exclude = ['usuario']
	
