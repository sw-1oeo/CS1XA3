import json
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

def login_user_view(request):
    print('request body', request.body)
    json_data = json.loads(request.body)
    print('json data', json_data)
    username = json_data.get('username') 
    password = json_data.get('password') 

    user = authenticate(request,username=username,
                                password=password)

    status_code = 401
    message = "Login failed"
    if user is not None:
        login(request,user)
        status_code = 200
        message = "Logged in"
        
    return JsonResponse({'message': message}, status=status_code)


def logout_user_view(request):
  logout(request)
  status_code = 200
  message = "Logged out"
  return JsonResponse({'message': message}, status=status_code)
  

