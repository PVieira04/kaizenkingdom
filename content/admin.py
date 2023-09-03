from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, Unit, Topic, QuizQuestion, QuizOption

@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('question_text')

@admin.register(QuizOption)
class QuizOptionAdmin(SummernoteModelAdmin):
    summernote_fields = ('option_text')