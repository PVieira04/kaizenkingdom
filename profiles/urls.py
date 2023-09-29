from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('update/', views.profile_update, name='profile_update'),
]
