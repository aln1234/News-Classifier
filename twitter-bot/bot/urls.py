from django.urls import path
from django.conf.urls import url

from bot import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('bota/', views.bota, name='bota'),
    path('botc/', views.botc, name='botc'),
    path('botb/', views.botb, name='botb'),
    path('', views.home, name='homepage'),



]
