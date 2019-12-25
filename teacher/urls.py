from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^teacher_index$', views.teacher_index_view),
    url(r'^teacher_course/', views.teacher_course_view),
    url(r'^course_index/', views.course_index_view),
    url(r'^course_add/', views.course_add_view),
]