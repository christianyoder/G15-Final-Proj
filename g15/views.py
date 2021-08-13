from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'g15/index.html')

def a1(request):
    return render(request, 'g15/P2/home.html')

def b(request):
    return render(request, 'g15/P2/explore.html')

def c(request):
    return render(request, 'g15/P2/addRoutine.html')

def d(request):
    return render(request, 'g15/P2/tracker.html')

def s1(request):
    return render(request, 'g15/P2/trackerDemo.html')

def e(request):
    return render(request, 'g15/P2/leaderboard.html')

def s2(request):
    return render(request, 'g15/P2/leaderboardDemo.html')    

def f(request):
    return render(request, 'g15/P2/social.html')

def room(request, room_name):
    return render(request, 'g15/room.html', {
        'room_name': room_name
    })