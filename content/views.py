from django.shortcuts import render
from django.views import generic
from .models import Course, Unit, Topic, QuizQuestion

class CourseList(generic.ListView):
    model = Course
    template_name = 'index.html'
    paginate_by = 6
