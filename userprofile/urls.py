from django.urls import path
from . import views

app_name='userprofile'

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.userRegisteration, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.profile, name="profile"),
]