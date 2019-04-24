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
    response_data = {'message': message}
    if user is not None:
        login(request, user)
        status_code = 200
        response_data['message'] = "Logged in"
        response_data['user_id'] = user.id
        
    return JsonResponse(response_data, status=status_code)


def logout_user_view(request):
    print('request.user', request.user)
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


def high_scores_view(request):
    query_set = UserProfile.objects.filter(max_score__gt=0).order_by('-max_score')
    print(query_set)
    high_scores = []
    for user_profile in query_set:
        high_scores.append({"username": user_profile.user.username, "max_score":user_profile.max_score})
    return JsonResponse({'highscores': high_scores})


def score_user_view(request):
    json_data=json.loads(request.body)

    score = json_data.get('score')
    userId = json_data.get('userId')
        
    status_code = 400
    message = "Unable to update score"

    user = User.objects.filter(id=userId).first()
    
    if user:
        status_code = 200
        if score > user.userprofile.max_score:
            user.userprofile.max_score = score
            user.userprofile.save()
            message = "New max score updated"
        else:
            message = "New score not higher than previous max"

    return JsonResponse({'message': message}, status=status_code)
