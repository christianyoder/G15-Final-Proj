from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.a1, name='home'),
    path('explore/', views.b, name='explore'),
    path('addRoutine/', views.c, name='addRoutine'),
    path('tracker/', views.d, name='tracker'),
    path('leaderboard/', views.e, name='leaderboard'),
    path('social/', views.f, name='social'),
    path('<str:room_name>/', views.room, name='room'),
]

