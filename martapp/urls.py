from django.contrib import admin
from django.urls import path,include
from martapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('register/',views.register,name='register'),
    path('forgot/',views.forgot,name='forgot'),
    path('post/',views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('view/<str:pk>/',views.view,name='view'),
    path('update/<str:pk>/',views.update,name='update'),
    path('deletepost/<str:pk>/',views.deletepost,name='deletepost'),
]