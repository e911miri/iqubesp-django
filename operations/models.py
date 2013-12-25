from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 100)
    desc = models.TextField()
    link = models.CharField(max_length= 200)
    testimonial = models.CharField(max_length= 200)
    active = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name