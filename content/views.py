from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Course, Unit, Topic, QuizQuestion

class CourseList(generic.ListView):
    model = Course
    template_name = 'course_list.html'
    paginate_by = 6

class CourseDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Course.objects
        course = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "course_detail.html",
            {
                "course": course
            }
        )

class UnitDetail(generic.ListView):
    model = Unit
    template_name = 'unit_list.html'
    paginate_by = 6