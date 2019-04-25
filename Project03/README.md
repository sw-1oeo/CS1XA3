# Project03

## Run on Server

ssh <username>@mac1xa3.ca
source /home/sunwooj/CS1XA3/Project03_env/bin/activate
cd /home/sunwooj/CS1XA3/Project03/django_project/

### Run Django server
python3 manage.py runserver localhost:10053

### Access Django admin 
https://mac1xa3.ca/e/sunwooj/admin/

### Play game
https://mac1xa3.ca/u/sunwooj/project3.html

Explain that the user needs to register and then log in so they can play
How to play the game

## Run Locally

git clone
cd <proj_name> # double check directories
create a virtualenv with python3
activate virtualenv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

To play game: open the login_page.html in a browser

### Curl examples for Django API

Note: The Django server must be running before calling the API

<log in>
#Log-in, success (username, password matches)
curl -vk -X POST -H "Content-Type: application/json" --data '{"username": "jerry", "password": "passP1234"}' https://mac1xa3.ca/e/sunwooj/accounts/login
=> {"message": "Logged in", "user_id": 2} <another terminal>
=> "POST /e/sunwooj/accounts/login/ HTTP/1.1" 200 38 <server terminal>

#Log-in, failed (username, password does not match)

=> {"message": "Login failed"}
=> "POST /e/sunwooj/accounts/login/ HTTP/1.1" 401 27

<log out>  @but logged out as who? @로그인 안된상태에 로그아웃 해도, 200 뜨는데?
curl -vk -X POST -H "Content-Type: application/json" https://mac1xa3.ca/e/sunwooj/accounts/logout
=> {"message": "Logged out"}
=> "POST /e/sunwooj/accounts/logout/ HTTP/1.1" 200 25               

<creation>
curl -vk -X POST -H "Content-Type: application/json" --data '{"username": "tomma", "password": "passP1234", "confirm_password":"passP1234"}' https://mac1xa3.ca/e/sunwooj/accounts/user/
=> 
=> “POST /e/sunwooj/accounts/user/ HTTP/1.1" 201 27

<highscore> @getting 301.. 
curl -vk -X GET -H "Content-Type: application/json" https://mac1xa3.ca/e/sunwooj/accounts/high_score/

<updatescore> @getting 404
You need a valid USER_ID based on an earlier request that created a user
curl -vk -X POST -H "Content-Type: application/json" --data '{"score": "4", "userId": "<USER_ID>"}' https://mac1xa3.ca/e/sunwooj/accounts/update_score/
