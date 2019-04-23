import json
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import UserProfile


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


def register_user_view(request):
    json_data = json.loads(request.body)
    
    username = json_data.get('username') 
    password = json_data.get('password')   
    confirm_password = json_data.get('confirm_password')


    status_code = 400
    if User.objects.filter(username=username).count() > 0:
        message = "Username not available"

    else:
        message = "Passwords do not match"

        if (password==confirm_password):
            new_user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=new_user, max_score=0)

            status_code = 201
            message = "User created"
    return JsonResponse({'message': message}, status=status_code)
