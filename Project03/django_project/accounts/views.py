import json
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import UserProfile


def login_user_view(request):
    # parse data as Json
    json_data = json.loads(request.body)
    username = json_data.get('username') 
    password = json_data.get('password') 

    user = authenticate(request,username=username,
                                password=password)

    status_code = 401 #anauthorized
    message = "Login failed"
    response_data = {'message': message}
    #only when username and password match with the exsiting user 
    if user is not None:
        login(request, user)
        status_code = 200 #ok
        response_data['message'] = "Logged in"
        response_data['user_id'] = user.id #user.id which is allocated for each username

    return JsonResponse(response_data, status=status_code)


def logout_user_view(request):
    logout(request)
    status_code = 200
    message = "Logged out"
    return JsonResponse({'message': message}, status=status_code)


def register_user_view(request):
    # parse data as Json
    json_data = json.loads(request.body)
    username = json_data.get('username')
    password = json_data.get('password')
    confirm_password = json_data.get('confirm_password')

    #status code 400: bad request 
    status_code = 400
    #If that user name is already taken, throws an error message
    if User.objects.filter(username=username).count() > 0:
        message = "Username not available"
    #password & confirm_password not matched, throws an error message
    else:
        message = "Passwords do not match"
        #password & confirm_password matched, creates user, and gets max_score=0 as a default
        if (password==confirm_password):
            new_user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=new_user, max_score=0)
            #201: created
            status_code = 201
            message = "User created"
    return JsonResponse({'message': message}, status=status_code)


def high_scores_view(request):
    #get query_set which has username and max_score in a descending order
    query_set = UserProfile.objects.filter(max_score__gt=0).order_by('-max_score')
    high_scores = []
    #iterate over query_set and append new queryset with max_score and username
    for user_profile in query_set:
        high_scores.append({"username": user_profile.user.username, "max_score":user_profile.max_score})
    return JsonResponse({'highscores': high_scores})


def score_user_view(request):
    # Parse data as JSON
    json_data=json.loads(request.body)

    score = json_data.get('score')
    userId = json_data.get('userId')

    status_code = 400
    message = "Unable to update score"
    #if passed in with a bad userId
    user = User.objects.filter(id=userId).first()

    if user:
        status_code = 200
        #if the score is greater than the user's previous max score, updates the score as the max score 
        if score > user.userprofile.max_score:
            user.userprofile.max_score = score
            user.userprofile.save()
            message = "New max score updated"
        else:
            message = "New score not higher than previous max"

    return JsonResponse({'message': message}, status=status_code)
