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
    fields = ('course', 'number', 'title', 'slug', 'description')

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_display = ('topic_name', 'unit_name', 'course_name')
    ordering = ('unit__course__title', 'unit__unit_number', 'number') # This changes default sorting
    fields = ('unit', 'number', 'title', 'slug', 'content')
    search_fields = ['title', 'unit__course__title', 'unit__title']
    list_filter = ('unit__course__title', 'unit__title')
    
    def course_name(self, obj):
        return obj.unit.course.title

    course_name.short_description = 'Course' # Custom column heading
    course_name.admin_order_field = 'unit__course__title' # Enable sorting options

    def unit_number(self, obj):
        return obj.unit.number
    
    def unit_name(self, obj):
        return f"Unit {obj.unit.number}: {obj.unit.title}"
    
    unit_name.short_description = 'Unit'
    unit_name.admin_order_field = 'unit__unit_number'
    
    def topic_name(self, obj):
        return f"Topic {obj.number}: {obj.title}"

    topic_name.short_description = 'Topic'
    topic_name.admin_order_field = 'number'

    # Override the get_queryset() function which runs every time django wants to display a list of topics from the database.
    def get_queryset(self, request):
        # Retrieve the default queryset - this includes all topics in the database.
        queryset = super().get_queryset(request)
        # Modify the queryset by ordering it in a specific way.
        queryset = queryset.order_by('unit__course__title', 'unit__unit_number', 'number')
        return queryset

@admin.register(QuizQuestion)
class QuizQuestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('question_text')