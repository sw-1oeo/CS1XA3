from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_user_view , name='login_user'),
    path('accounts/logout/', views.logout_user_view , name='logout_user'),
    path('accounts/user/', views.register_user_view , name='register_user'),
    path('accounts/score/', views.score_user_view , name='update_score'),
    path('accounts/high_score/', views.high_scores_view , name='high_score'),
]


