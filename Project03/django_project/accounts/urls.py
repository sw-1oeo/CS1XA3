from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_user_view , name='login_user'),
    path('accounts/logout/', views.logout_user_view , name='logout_user'),
]


