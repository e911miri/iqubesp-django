from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from operations.models import Course
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect('/admin')
        context = {
            'courses': Course.objects.all(),
            'tasks': None,
        }
        template_path = "home/student_home.djhtml"
    else:        
        context= {
            'main': "The Journey of an IT GURU Statts with one skill",
            "block1": "Learning in sdp is having your mentor right next to you - Kola",
            "block2": "At SDP, learning has never been more fun - Wande",
            "block3": "I often ask myself why it is so cheap, 3months - 5k? it's just awesome - Orimolade M."
        }        
        template_path = "home/index.djhtml"
    return render(request, template_path, context)