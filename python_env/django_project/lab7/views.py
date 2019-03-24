from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def returnPost(request):
   username = request.POST.get("username","")
   password  = request.POST.get("password","")
   repassword = request.POST.get("repassword","")
   if username == "Jimmy" and password == "Hendrix" and repassword == password:
      return HttpResponse("Cool")
   return HttpResponse("Bad User Name")

#If the user name is Jimmy and the password is Hendrix, the server should respond Cool. Otherwise respond Bad User Name
# Create your views here.
