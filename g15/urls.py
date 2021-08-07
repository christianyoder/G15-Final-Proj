from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a1/', views.a1, name='home'),
    path('b1/', views.b, name='explore'),
    path('c1/', views.c, name='addRoutine'),
    path('d1/', views.d, name='tracker'),
    path('e1/', views.e, name='leaderboard'),
    path('f1/', views.f, name='social'),
]

