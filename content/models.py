from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='')
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
        return f"{self.unit.course.title} - Unit {self.unit.number}: {self.unit.title} - Topic {self.number}: {self.title}"

class QuizQuestion(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_1 = models.CharField(max_length=200, blank=True, null=True)
    option_2 = models.CharField(max_length=200, blank=True, null=True)
    option_3 = models.CharField(max_length=200, blank=True, null=True)
    option_4 = models.CharField(max_length=200, blank=True, null=True)
    correct_option = models.PositiveSmallIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], blank=True, null=True)

    class Meta:
        unique_together = ('topic', 'question_text')
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'

    def __str__(self):
        return self.question_text

    def clean(self):
        options = [self.option_1, self.option_2, self.option_3, self.option_4]
        unique_options = list(filter(None, set(options)))
        if len(unique_options) < len(options):
            raise ValidationError("Options 1 - 4 must be unique.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)