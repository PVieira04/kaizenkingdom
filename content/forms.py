from django import forms
from .models import Course, Unit, Topic

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class EditTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']