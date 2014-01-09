from django.shortcuts import render
from operations.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from students.models import StudentCourse

@login_required
def home(request):
    context = {
            'courses': Course.objects.filter(),
            'scourses': StudentCourse.objects.filter(student=request.user),
            'tasks': None,
        }
    template_path = "students/home.djhtml"
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/students/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.djhtml", {
        'form': form,
    })

def logout_view(request):
    logout(request)
