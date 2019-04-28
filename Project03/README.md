# Project03: Tom & Jerry game with Django

## Run on Server
Use your macid to ssh into the server, activate virtual environment, and change directory into django_project.

    ssh <macid>@mac1xa3.ca
    source /home/sunwooj/CS1XA3/Project03_env/bin/activate
    cd /home/sunwooj/CS1XA3/Project03/django_project/


### Run Django server
Now you are prepared to run Django server. 

    python3 manage.py runserver localhost:10053

### Play game

    https://mac1xa3.ca/u/sunwooj/project3.html
                       or
    https://mac1xa3.ca/e/sunwooj/static/project3.html

This game is set to be served at both the school server and django server. Choose either one you like to play the game. 
You first need to register and log-in. Once you are logged-in, game automatically starts. You can move Jerry up, down, right, and left side using the four arrow keys. Your goal is to eat cheese when it pops up at any random position to score up, while trying not to get caught by Tom. When you get caught by Tom, game is over. You can see other user's max score if you click "See high scores". Don't forget to log-out, when you are done with playing.

### Access Django admin 

    https://mac1xa3.ca/e/sunwooj/admin/

You need a super user account to access to the Django admin. Follow the direction under "Run on Server". Use the command to create super user. 

    python manage.py createsuperuser


## Run Locally
In your terminal, do a git clone, cd into the project repo, create and activate a python virtual environment. You need to do python manage.py migrate this time, since data base changes on another server.

    git clone https://github.com/sw-1oeo/CS1XA3.git
    cd CS1XA3/
    python3 -m venv pythonia_env 
    cd pythonia_env
    source bin/activate
    cd ../Project03
    pip install -r requirements.txt
    cd django_project/
    python manage.py migrate
    python manage.py runserver 

To play game: open the login_page.html in a browser


## Curl examples for Django API with Each feature

Note: The Django server must be running before calling the API
Note: Try curl command on another terminal, and check it with the terminal with Django server on.


## Log-in Feature
When the username and password match with the existing user, gets {"message": "Logged in", "user_id": 2}, and curl command receives a Http response 200, which means okay. If it does not match, gets {"message": "Login failed"}, and curl command receives a response 401 which means unauthorized. 

### Curl command example:

    curl -vk -X POST -H "Content-Type: application/json" --data '{"username": "jerry", "password": "passP1234"}' https://mac1xa3.ca/e/sunwooj/accounts/login


## Log-out Feature
There is no any parameter. Just http request sent to server for log out to be functioning. Once requested, gets {"message": "Logged out"}, and curl command reveives a Http response of 200, meaning okay. 

### Curl command example:

    curl -vk -X POST -H "Content-Type: application/json" https://mac1xa3.ca/e/sunwooj/accounts/logout


## Registration feature
For a new user to create a new account, username, password, and confirm password have to be passed in. Three conditions considered for this feature. When the username is already taken by another user, it will throw {"message": "Username not available"} with a response of 400, meaning bad request. Then, only if password matches with confirm_password, it will throw {"message": "User created"} with a reponse of 201, meaning sucessfully created. Else, in case where user name is valid but password and confirm password do not match, it will throw {"message": "Passwords do not match"} with a http reponse of 400 meaning bad request. 

### Curl command example:

    curl -vk -X POST -H "Content-Type: application/json" --data '{"username": "tomma", "password": "passP1234", "confirm_password":"passP1234"}' https://mac1xa3.ca/e/sunwooj/accounts/user/


## Max score feature
This feature is scoring through UserProfile using the foreign key to the django User model. Queryset with field name, username and max-score is used here. Since the data is retrieved from the server, GET is used. In the function from views.py, .filter is used so we can only get score greater than zero, and .order_by("-max_score") is used so we can get scores decending from the hightest. When requested, for example, gets query sets of {"highscores": [{"username": "pink3", "max_score": 4}, {"username": "pink1", "max_score": 3}, {"username": "pink2", "max_score": 1}]} with Http resonse of 200, meaning okay. 
   
### Curl command example:

    curl -vk -X GET -H "Content-Type: application/json" https://mac1xa3.ca/e/sunwooj/accounts/high_score/


## Update score feature
You need a valid USER_ID based on an earlier request that created a user. POST is used since the data is sent to the server. For this feature, valid userId should be passed in, and if the score is greater than user's existing max score, gets {"message": "New max score updated"} with http response of 200, meaning okay. If it is not greater, gets {"message": "New score not higher than previous max"}, and when invalid userId is passed in, gets {"message": "Unable to update score"}, both receiving Http response of 400 meaning bad request.   

### Curl command example:

    curl -vk -X POST -H "Content-Type: application/json" --data '{"score": 4,"userId": "<USER_ID>"}' https://mac1xa3.ca/e/sunwooj/accounts/score/


## Features from client-side: 

Javascript is mainly used for the client side. 

* Keyboard event: Used onkeydown & onkeyup event to move object in four directions within the specified condition and range, using Boolean function. 

* Random number: To draw an object in a different x or y position randomly, Math.random() was used to get any number between 0~1, and then implemented this to get random index from the List with x or y position elements.

* setInterval, clearInterval: Used setInterval to call the game function in every 0.01s as a frame, and clearInterval is used to end the game.

* Animation (getting rid of tom and cheese): Used list.splice function in js, to remove current item from an array, so that tom or cheese can be got rid of from the game page when Tom gets to the right end of the game box or when Cheese is collided by Jerry.

* Collision detection: Set the condition for two objects that are overlapped which means they collide. Used this collision status for situation when Jerry eats Cheese or Jerry caught by Tom.

* Animation (toggle between login page and creation page): Used Jquery .animation and toggle to hide creation form and then change it to visible mode when it is clicked.

* Using the serverCall function from jerry.js, made API call to the Django server. Used this function to make API call to login user, create user, logout user, update the score, and get the max score of all other users. To describe more in detail, this function has four parameters which are path, method, requestData, and callback. Path is the url path after /accounts/, so for /accounts/login, login should be passed in. The method parameter is for HTTP method. So it is either GET or POST. The requesdData is Data to be passed to server. For last, callback function will be called whenever request is completed. So using this function, API call can be made, JSON data can be parsed from response, and JSON request can be made to the server. 
