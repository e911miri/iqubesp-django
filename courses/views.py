from django.shortcuts import render, redirect
from operations.models import Course
from django.contrib.auth.decorators import login_required
from students.models import StudentCourse

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
    course = Course.objects.get(pk=course_id)
    sc = StudentCourse.objects.create(student=request.user, course=course, invite_reason = 'automated', paid=False)
    sc.save()
    
    return redirect('/students')
#     if request.POST:
#         course = Course.objects.get(pk=course_id)
#         StudentCourse.objects.create(student=request.user, course=course, invite_reason = 'automated', paid=False)
#         return redirect('/students')
#     context = {
#        'courses': Course.objects.get(pk=course_id)
#     }
#     template_path = "courses/register.djhtml"
#     return render(request, template_path, context)