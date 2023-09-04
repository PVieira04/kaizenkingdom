from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, Unit, Topic, QuizQuestion

@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')

@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_display = ('course_name', 'unit', 'number', 'title')

    def unit_number(self, obj):
        return obj.unit.number
    
    def course_name(self, obj):
        return obj.unit.course.title
    
    unit_number.short_description = 'Unit Number'  # Set a custom column header for unit_number
    course_name.short_description = 'Course Name'  # Set a custom column header for course_name

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('unit__course__title', 'unit__unit_number', 'number')
        return queryset

@admin.register(QuizQuestion)
class QuizQuestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('question_text')