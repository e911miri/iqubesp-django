from django.contrib import admin
from operations.models import Course, StudentTestimony
from students.models import StudentCourse, Payment
# Register your models here.

admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(Payment)
admin.site.register(StudentTestimony)