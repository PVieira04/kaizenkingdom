from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<slug:course_slug>/', views.CourseDetail.as_view(), name='course_detail'),
    path('<slug:course_slug>/<slug:unit_slug>/', views.UnitDetail.as_view(), name='unit_detail'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/edit/', views.EditTopic.as_view(), name='edit_topic'),
]
