from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Course, Unit, Topic, QuizQuestion

class CourseList(generic.ListView):
    model = Course
    template_name = 'course_list.html'
    paginate_by = 6

class CourseDetail(View):
    def get(self, request, course_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        courses = Course.objects.all()
        units = Unit.objects.filter(course=course)
        context = {
            'course' : course,
            'units' : units,
        }
        return render(request, "course_detail.html", context)

class UnitList(generic.ListView):
    model = Unit
    template_name = 'unit_list.html'
    paginate_by = 6

class UnitDetail(View):
    def get(self, request, course_slug, unit_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug, course=course)
        units = Unit.objects.all()
        topics = Topic.objects.filter(unit=unit)
        context = {
                "course" : course,
                "unit" : unit,
                "topics" : topics,
            }
        return render(request, "unit_detail.html", context)

class TopicList(generic.ListView):
    model = Topic
    template_name = 'topic_list.html'
    paginate_by = 6

class TopicDetail(View):
    def get(self, request, course_slug, unit_slug, topic_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug)
        topic = get_object_or_404(Topic, slug=topic_slug, unit=unit)
        topics = Topic.objects.all()
        context = {
                "topic" : topic,
                "unit" : unit,
                "course" : course,
            }
        return render(request, "topic_detail.html", context)