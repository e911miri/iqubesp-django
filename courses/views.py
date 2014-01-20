from django.shortcuts import render, redirect, get_object_or_404
from operations.models import Course
from django.contrib.auth.decorators import login_required
from students.models import StudentCourse
from django.views import generic

# Create your views here.
class index(generic.ListView):
    template_name = 'courses/index.djhtml'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return the last five published polls."""
        return Course.objects.all()

def details(request, id, slug):
    context = {
       'course': get_object_or_404(Course, pk=id)
    }
    template_path = "courses/details.djhtml"
    return render(request, template_path, context)

@login_required
def register(request, id, slug):
    if request.POST:
        course = get_object_or_404(Course, pk=id)
        StudentCourse.objects.create(student=request.user, course=course, invite_reason = 'automated', paid=False)
        return redirect('/students')
    context = {
       'course': get_object_or_404(Course, pk=id)
    }
    template_path = "courses/register.djhtml"
    return render(request, template_path, context)