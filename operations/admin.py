from django.contrib import admin
from operations.models import Course, StudentTestimony
from students.models import StudentCourse, Payment
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'prerequisites', 'active']
    
class StudentTestimonyAdmin(admin.ModelAdmin):
    list_display = ['name', 'testimony', 'page']
    
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentCourse)
admin.site.register(Payment)
admin.site.register(StudentTestimony, StudentTestimonyAdmin)