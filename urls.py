from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login,logout

from Aeropuerto import settings #Importa el archivo de settings para STATIC_DOC_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Aeropuerto.MainApp.views',(r'^register/$','registercommon'),(r'^contact/$','contact'),(r'^search/$','searchdest'),(r'^registerstaff/$','registerstaff'),(r'^reservation/$','ticketreserv'),(r'^logout/$', 'logout'),(r'^profile/$','profile'),
    # Example:
    # (r'^Aeropuerto/', include('Aeropuerto.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

#Patron para archivos estaticos
urlpatterns += patterns('',(r'^sitemedia/(?P<path>.*)$', 'django.views.static.serve',
{'document_root': settings.STATIC_DOC_ROOT}),
)

urlpatterns += patterns('',(r'^admin/(.*)', admin.site.root),
(r'^media/admin/(?P<path>.*)$','django.views.static.serve',
{'document_root':'/home/frncsc/Django-1.1.1/Aeropuerto/Templates/admin/'}),
) #Cambio

urlpatterns += patterns('',(r'^success/$',direct_to_template,{'template':'Success.html'}),
(r'^accounts/profile/$',direct_to_template,{'template':'LoggedIn.html'}),
(r'^loggedout/$',direct_to_template,{'template':'LoggedOut.html'}),
(r'^home/$',direct_to_template,{'template':'Home.html'}),
(r'^stafffail/$',direct_to_template,{'template':'StaffLoginFail.html'}),
(r'^loginfail/$',direct_to_template,{'template':'RequiresLogin.html'}),
(r'^stafflogin/$',direct_to_template,{'template':'StaffLogin.html'}),
(r'^successreserv/$',direct_to_template,{'template':'SuccessReserv.html'}),
)

urlpatterns += patterns('',
	(r'^login/$', login,{'template_name': 'Login.html'}),
)
