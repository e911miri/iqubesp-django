from django.shortcuts import render
from operations.models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
       'courses': Course.objects.all()
    }
    template_path = "courses/index.djhtml"
    return render(request, template_path, context)

def details(request, course_id):
    context = {
       'course': Course.objects.get(pk=course_id)
    }
    template_path = "courses/details.djhtml"
    return render(request, template_path, context)

@login_required
def register(request, course_id):
    context = {
       'courses': Course.objects.get(pk=course_id)
    }
    template_path = "courses/register.djhtml"
    return render(request, template_path, context)