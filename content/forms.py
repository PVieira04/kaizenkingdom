from django import forms
from .models import Course, Unit, Topic

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class EditTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']