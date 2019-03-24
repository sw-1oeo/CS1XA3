from django.urls import path
from . import views

urlpatterns = [
    path('lab7/', views.returnPost , name='lab7 function'),
]
