from django.db import models
from django.utils.text import slugify
from sdp.constants import course_categories

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 100)
    desc = models.TextField()
    link = models.CharField(max_length= 200)
    testimonial = models.CharField(max_length= 200)
    active = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    category = models.CharField(max_length=10, choices=course_categories)
    image = models.ImageField(upload_to="courses")
    
    class Meta:
        verbose_name_plural = "Courses"
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.name))
        super(Course, self).save(*args, **kwargs)
        

class StudentTestimony(models.Model):
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to="testimonies")
    testimony = models.TextField()
    page = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Stundent Testimonies"