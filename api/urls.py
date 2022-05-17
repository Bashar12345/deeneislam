from django.urls import path,include
from . import views

from rest_framework import routers


router =routers.DefaultRouter()
router.register("articles", views.article_api_view)


urlpatterns = [
    #path('', views.product_list_view.as_view(), name='RED-home'),
    #path('api/', views.api_home, name='api-index'), 
    path('',include(router.urls))
    
]