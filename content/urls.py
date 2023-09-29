from . import views
from django.urls import path

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('<slug:course_slug>/', views.CourseDetail.as_view(), name='course_detail'),
    path('courses/create-course/', views.CreateCourse.as_view(), name='create_course'),
    path('<slug:course_slug>/delete/', views.DeleteCourse.as_view(), name='delete_course'),
    path('<slug:course_slug>/edit/', views.EditCourse.as_view(), name='edit_course'),
    path('<slug:course_slug>/add-unit/', views.AddUnit.as_view(), name='add_unit'),
    path('<slug:course_slug>/<slug:unit_slug>/', views.UnitDetail.as_view(), name='unit_detail'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/edit/', views.EditTopic.as_view(), name='edit_topic'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/delete/', views.DeleteTopic.as_view(), name='delete_topic'),
    path('<slug:course_slug>/<slug:unit_slug>/<slug:topic_slug>/quiz/', views.Quiz.as_view(), name='quiz'),
]
