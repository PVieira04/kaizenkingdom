from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course
from .models import Unit
from .models import Topic

@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')