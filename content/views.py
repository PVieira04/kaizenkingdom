from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.views import generic, View
from django.urls import reverse
from random import sample
from .models import Course, Unit, Topic, QuizQuestion
from .forms import CourseForm, UnitForm, TopicForm
from profiles.models import CustomUser

class CourseList(generic.ListView):
    model = Course
    template_name = 'course_list.html'
    paginate_by = 6
    extra_context = {"form_name": "Course"}

class CourseDetail(View):
    def get(self, request, course_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        courses = Course.objects.all()
        units = Unit.objects.filter(course=course)
        context = {
            'course' : course,
            'units' : units,
        }
        extra_context = {"form_name": "Course"}
        return render(request, "course_detail.html", context)

class CreateCourse(View):
    def get(self, request):
        if request.user.customuser.account_type == 'teacher':
            form = CourseForm()
            context = {
                'form' : form,
            }
            return render(request, 'create_course.html', context)
        else: return redirect('course_list')
    
    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid() and request.user.customuser.account_type == 'teacher':
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('course_detail', course_slug=course.slug)
        else:
            context = {
                'form' : form,
            }
            return render(request, 'create_course.html', context)

class EditCourse(View):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        if course.author != request.user:
            return redirect('course_detail', course_slug=course.slug)
        
        form = CourseForm(instance=course)
        edit_url = edit_url = reverse('edit_course', args=[course_slug])
        context = {
            "form" : form,
            "course" : course,
            "edit_url" : edit_url,
        }
        return render(request, 'edit_course.html', context)
    
    def post(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        if course.author != request.user:
            return redirect('course_detail', course_slug=course.slug)
        
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_slug=course.slug)
        
        context = {
            "form" : form,
            "course" : course,
        }
        return render(request, 'edit_course.html', context)

class DeleteCourse(View):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        context = {
            'course' : course
        }
        if request.user.id != course.author.id:
            return redirect('course_detail', context)
        return render(request, 'delete_course.html', context)

    def post(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        context = {
            'course' : course
        }
        if request.user.id != course.author.id:
            return redirect('course_detail', context)
        course.delete()
        return redirect('course_list')

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
        print(f'topics: {topics}')
        return render(request, "unit_detail.html", context)

class AddUnit(View):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        if request.user.id == course.author.id:
            form = UnitForm()
            context = {
                'form' : form,
                'course' : course,
            }
            return render(request, 'add_unit.html', context)
        else: return redirect('course_detail', course_slug=course.slug)
    
    def post(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.course = course
            max_unit_number = Unit.objects.filter(course=course).aggregate(max_number=Max('number'))['max_number']
            if max_unit_number is not None:
                unit.number = max_unit_number + 1
            else:
                unit.number = 1
            unit.save()
            return redirect('course_detail', course_slug=course.slug)
        else:
            context = {
                'form' : form,
                'course' : course,
            }
            return render(request, 'add_unit.html', context)

class EditUnit(View):
    def get(self, request, course_slug, unit_slug):
        unit = get_object_or_404(Unit, slug=unit_slug)
        course = unit.course
        if request.user.id == course.author.id:
            form = UnitForm(instance=unit)
            context = {
                'form': form,
                'unit': unit,
                'course': course,
            }
            return render(request, 'edit_unit.html', context)
        else:
            return redirect('course_detail', course_slug=course.slug)

    def post(self, request, course_slug, unit_slug):
        unit = get_object_or_404(Unit, slug=unit_slug)
        course = unit.course
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid() and request.user.id == course.author.id:
            unit = form.save(commit=False)
            unit.save()
            return redirect('unit_detail', course_slug=course.slug, unit_slug=unit.slug)
        else:
            context = {
                'form': form,
                'unit': unit,
                'course': course,
            }
            return render(request, 'edit_unit.html', context)

class DeleteUnit(View):
    def get(self, request, course_slug, unit_slug):
        unit = get_object_or_404(Unit, slug=unit_slug)
        if request.user.id != unit.course.author.id:
            return redirect('unit_detail', course_slug=unit.course.slug, unit_slug=unit.slug)
        return render(request, 'delete_unit.html', {'unit': unit})

    def post(self, request, course_slug, unit_slug):
        unit = get_object_or_404(Unit, slug=unit_slug)
        if request.user.id != unit.course.author.id:
            return redirect('unit_detail', course_slug=unit.course.slug, unit_slug=unit.slug)
        unit.delete()
        return redirect('course_detail', course_slug=course_slug)

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

class AddTopic(View):
    def get(self, request, course_slug, unit_slug):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug)
        if request.user.id == course.author.id:
            form = TopicForm()
            context = {
                'form' : form,
                'course' : course,
                'unit' : unit,
            }
            return render(request, 'add_topic.html', context)
        else: return redirect('unit_detail', course_slug=course.slug, unit_slug=unit.slug)
    
    def post(self, request, course_slug, unit_slug):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug)
        form = TopicForm(request.POST)
        if form.is_valid() and request.user.id == course.author.id:
            topic = form.save(commit=False)
            topic.unit = unit
            max_topic_number = Topic.objects.filter(unit=unit).aggregate(max_number=Max('number'))['max_number']
            if max_topic_number is not None:
                topic.number = max_topic_number + 1
            else:
                topic.number = 1
            topic.save()
            return redirect('unit_detail', course_slug=course.slug, unit_slug=unit.slug)
        else:
            context = {
                'form' : form,
                'course' : course,
                'unit' : unit,
            }
            return render(request, 'add_topic.html', context)

class EditTopic(View):
    def get(self, request, course_slug, unit_slug, topic_slug):
        course = get_object_or_404(Course, slug=course_slug)
        unit = get_object_or_404(Unit, slug=unit_slug, course=course)
        topic = get_object_or_404(Topic, slug = topic_slug, unit=unit)
        if topic.unit.course.author != request.user:
            return redirect('topic_detail', course_slug=topic.unit.course.slug, unit_slug=topic.unit.slug, topic_slug=topic.slug)
        
        form = TopicForm(instance=topic)
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
            return redirect('topic_detail', course_slug=topic.unit.course.slug, unit_slug=topic.unit.slug, topic_slug=topic.slug)
        
        form = TopicForm(request.POST, instance=topic)
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
        topic = get_object_or_404(Topic, slug=topic_slug)
        if request.user.id != topic.unit.course.author.id:
            return redirect('topic_detail', course_slug=topic.unit.course.slug, unit_slug=topic.unit.slug, topic_slug=topic.slug)
        return render(request, 'delete_topic.html', {'topic': topic})

    def post(self, request, course_slug, unit_slug, topic_slug):
        topic = get_object_or_404(Topic, slug=topic_slug)
        if request.user.id != topic.unit.course.author.id:
            return redirect('topic_detail', course_slug=topic.unit.course.slug, unit_slug=topic.unit.slug, topic_slug=topic.slug)
        topic.delete()
        return redirect('unit_detail', course_slug=course_slug, unit_slug=unit_slug)

class Quiz(View):
    def get(self, request, course_slug, unit_slug, topic_slug):
        questions = QuizQuestion.objects.filter(topic__slug=topic_slug)

        random_questions = sample(list(questions), min(len(questions), 5))

        context = {
            "questions" : random_questions,
        }

        return render(request, "quiz.html", context)