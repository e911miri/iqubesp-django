from django.shortcuts import render
from operations.models import Course
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
            'courses': Course.objects.all(),
            'tasks': None,
        }
    template_path = "students/home.djhtml"
    return render(request, template_path, context)