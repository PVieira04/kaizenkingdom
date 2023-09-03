from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Unit(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
    number = models.PositiveIntegerField()
    description = models.TextField()
    
    class Meta:
        ordering = ['number']
        unique_together = ('course', 'title')

    def __str__(self):
        return f"{self.course.title} - Unit {self.number}: {self.title}"

class Topic(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()

    class Meta:
        unique_together = ('unit', 'title')
        ordering = ['number']
    
    def __str__(self):
        return f"{self.unit.course.title} - {self.unit.title} - Topic {self.number}: {self.title}"