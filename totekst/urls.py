#from  django.urls import path
from django.conf.urls import include, url
from . import views

#app_name = 'totekst'
urlpatterns = [
    url(r'^$',views.login,name='login'),
    url('convert',views.convert,name='convert'),
    url(r'^(?P<email>[^/]+)/home/$',views.home,name='home'),
    url(r'^loaderio-*', views.loaderio, name='loaderio')
]