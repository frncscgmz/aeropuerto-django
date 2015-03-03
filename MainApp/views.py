from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.contrib import auth
from django import forms
from models import UserCreationFormExtended,Destinos,Reservacion
from Aeropuerto.MainApp.forms import ContactForm
from Aeropuerto.MainApp.models import ReservationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def registercommon(request): #Vista para registar usuario comun
	if request.method == 'POST':
		form = UserCreationFormExtended(request.POST) #Forma generica de registro
		if form.is_valid():
			new_user = form.save()
			new_user.groups.add('Common') #Agregar a grupo
			new_user.is_active = True
			new_user.is_authenticated = True
			new_user = form.save()
			new_user.save()
			new_user = form.save()
			return HttpResponseRedirect("/success/") 
	else:
		form = UserCreationFormExtended()
	return render_to_response("Register.html",{
		'form':form,
	})

def contact(request):
	if not request.user.is_authenticated(): #Si el usuario no esta logeado redirige la pagina al Login
		return HttpResponseRedirect('/login/?next=%s' % request.path)

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email''noreply@example.com'),
				['about.blanked@gmail.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': "I love your site!"}
		)
	return render_to_response('Contact.html',{'form':form})

def login(request): #Vista para auntetificar
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		#Password correcto y el usuario esta activo
		auth.login(request,user)
		#Redirecciona a la pagina de que funciono
		return HttpResponseRedirect("/loggedin/")
	else:
		#Muestra pagina con error
		#return HttpResponseRedirect("/account/invalid/")
		return render_to_response("LoggedIn.html")

def logout (request):
	auth.logout(request)
	#Redirecciona a la pagina de exito
	return HttpResponseRedirect("/loggedout/")

def searchdest(request):
	query = request.GET.get('q','')
	if query:
		qset = (
			Q(nombre__icontains=query)|
			Q(origen__icontains=query)|
			Q(destino__icontains=query)
		)
		results = Destinos.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("Search.html",{"results":results,"query":query})

def registerstaff(request): #Vista para registar usuario de staff nuevo
	if not request.user.is_superuser: 
		return HttpResponseRedirect("/stafffail/")

	else:

		if request.method == 'POST':
			form = UserCreationFormExtended(request.POST) #Forma generica de registro
			if form.is_valid():
				new_user = form.save()
				new_user.groups.add('Staff') #Agregar a grupo
				new_user.is_staff = True #Solo el staff puede accesar al sitio de adminnistracion
				new_user = form.save()
				#new_user.is_active = True			
				return HttpResponseRedirect("/success/") 
		else:
			form = UserCreationFormExtended()
		return render_to_response("Register.html",{
		'form':form,
	})

#@login_required
def ticketreserv(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		if request.method =='POST':
			form = ReservationForm(request.POST)
			if form.is_valid():
				temp = form.save()
				return HttpResponseRedirect("/successreserv/")
			else:
				return HttpResponseRedirect('e=invalid')
		else:
			form = ReservationForm()
		return render_to_response('Reservation.html',{"form":form})#,"results":results})

def stafflogin(request): #Vista para auntetificar
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active and user.is_staff:
		#Password correcto y el usuario esta activo
		auth.login(request,user)
		#Redirecciona a la pagina de que funciono
		return HttpResponseRedirect("/admin/")
	else:
		#Muestra pagina con error
		#return HttpResponseRedirect("/account/invalid/")
		return render_to_response("LoggedIn.html")

def profile(request):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/?next=%s' % request.path)

	user = request.user
	results = Reservacion.objects.filter(usuario=user)
	return render_to_response("Profile.html",{"results":results})#,"query":query})
