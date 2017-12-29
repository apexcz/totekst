from  django.urls import path
from . import views

app_name = 'totekst'
urlpatterns = [
    path('',views.login,name='login'),
    path('login_post',views.login_post,name='login_post'),
    path('home/<str:email>',views.home,name='home'),
]