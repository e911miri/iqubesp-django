from django.shortcuts import render
from operations.models import Course


def home(request):
    context = {
            'courses': Course.objects.all(),
            'tasks': None,
        }
    template_path = "home/student_home.djhtml"
    return render(request, template_path, context)

def login(request, provider_name):
    pass