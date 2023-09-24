from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from .models import Course, Unit, Topic, QuizQuestion
from .forms import EditTopicForm

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

class EditTopic(View):
    def get(self, request, course_slug, unit_slug, topic_slug):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug, course=course)
        topic = get_object_or_404(Topic, slug = topic_slug, unit=unit)
        if topic.unit.course.author != request.user:
            return HttpResponseForbidden("Only the author may edit this topic.")
        
        form = EditTopicForm(instance=topic)
        edit_url = edit_url = reverse('edit_topic', args=[course_slug, unit_slug, topic_slug])
        context = {
            "form" : form,
            "topic" : topic,
            "edit_url" : edit_url,
        }
        return render(request, 'edit_topic.html', context)
    
    def post(self, request, course_slug, unit_slug, topic_slug):
        topic = get_object_or_404(Topic, slug=topic_slug)
        if topic.unit.course.author != request.user:
            return HttpResponseForbidden("Only the author may edit this topic.")
        
        form = EditTopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', course_slug=topic.unit.course.slug, unit_slug=topic.unit.slug, topic_slug=topic.slug)
        
        context = {
            "form" : form,
            "topic" : topic,
        }
        return render(request, 'edit_topic.html', context)

class DeleteTopic(View):
    def get(self, request, course_slug, unit_slug, topic_slug):
        # Fetch the topic to be deleted and display a confirmation page
        topic = get_object_or_404(Topic, slug=topic_slug)
        return render(request, 'delete_topic.html', {'topic': topic})

    def post(self, request, course_slug, unit_slug, topic_slug):
        # Perform the deletion of the topic
        topic = get_object_or_404(Topic, slug=topic_slug)
        topic.delete()
        return redirect('unit_detail', course_slug=course_slug, unit_slug=unit_slug)