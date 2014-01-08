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

def login_view(request):
    if request.POST:        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                return render(request, "auth/login.djhtml", {})
        else:
            # Return an 'invalid login' error message.
            return None
    else:
        return render(request, "auth/login.djhtml", {})

def register_view(request):
    if request.POST:        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                return render(request, "auth/login.djhtml", {})
        else:
            # Return an 'invalid login' error message.
            return None
    else:
        return render(request, "auth/register.djhtml", {})

def logout_view(request):
    logout(request)
