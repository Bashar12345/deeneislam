from django.urls import path
from . import views



urlpatterns = [
    #path('', views.product_list_view.as_view(), name='RED-home'),
    path('', views.index, name='RED-index'),  
    path('home/', views.home, name= 'RED-home'),
    path('donate/', views.donate, name='RED-donate'),                         #urls path address string 
    path('about/', views.about, name='RED-about'), 

    path('history/', views.history, name='RED-history'), 
    path('haddits/', views.haddits, name='RED-haddits'), 
    path('quran/', views.quran, name='RED-quran'), 
    path('science/', views.science, name='RED-science'), 
    path('local/', views.local, name='RED-local'), 
    path('news/', views.you_dont_know, name='RED-news'), 

    
    
]