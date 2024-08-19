from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('luis/', views.luis, name='luis'),
    path('', views.home, name='home'),
    path('rog/', views.rog, name='rog'),
    path('gael/', views.gael, name='gael'),
    path('fab', views.fab, name='fab'),
    path('samantha/', views.samantha, name='samantha'),
    path('fatt/', views.fatt, name='fatt'),
    path('samaria/', views.samaria, name='samaria/'),
]