from django.contrib.auth import get_user_model
from django.urls import path
from boogie.rest import rest_api
from django.contrib.auth import views as auth_views

from . import views

# Inclui o modelo User na API
rest_api(get_user_model())

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    
]
