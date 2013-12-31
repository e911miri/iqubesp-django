from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 100)
    desc = models.TextField()
    link = models.CharField(max_length= 200)
    testimonial = models.CharField(max_length= 200)
    active = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Courses"
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.name))
        super(Course, self).save(*args, **kwargs)