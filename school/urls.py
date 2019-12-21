from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^test$', views.test),
    url(r'^$', views.index_view),
    url(r'^index$', views.index_view),
    url(r'^about$', views.about_view),
    url(r'^courses$', views.courses_view),
    url(r'^teachers$', views.teachers_view),
    url(r'^events$', views.events_view),
    url(r'^course-single$', views.course_single_view),
    url(r'^gallery$', views.gallery_view),
    url(r'^news$', views.news_view),
    url(r'^contact$', views.contact_view),
]