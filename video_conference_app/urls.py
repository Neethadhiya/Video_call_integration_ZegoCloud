from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login_view/',views.login_view,name='login_view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('meeting/',views.video_call,name='meeting'),
    path('join_room/',views.join_room,name='join_room'),
    path('logout/',views.logout_view,name='logout'),
]