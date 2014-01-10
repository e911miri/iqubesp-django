from django.shortcuts import render
from operations.models import Course
from django.contrib.auth.decorators import login_required
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
