from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('logout/',views.logoutUser, name="logout"),
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('profile/<str:pk>/',views.userProfile,name='userProfile'),
    path('createRoom/',views.createRoom,name='createRoom'),
    path('updateRoom/<str:pk>/',views.updateRoom,name='updateRoom'),
    path('deleteRoom/<str:pk>/',views.deleteRoom,name='deleteRoom'),
    path('deleteMessage/<str:pk>/',views.deleteMessage,name='deleteMessage'),
    path('updateUser/',views.updateUser,name='updateUser'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),
]