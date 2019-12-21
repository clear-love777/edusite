from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "school/test.html")


def index_view(request):
    return render(request, "school/index.html")


def about_view(request):
    return render(request, "school/about.html")


def courses_view(request):
    return render(request, "school/courses.html")


def teachers_view(request):
    return render(request, "school/teachers.html")


def events_view(request):
    return render(request, "school/events.html")


def course_single_view(request):
    return render(request, "school/course-single.html")


def gallery_view(request):
    return render(request, "school/gallery.html")


def news_view(request):
    return render(request, "school/news.html")


def contact_view(request):
    return render(request, "school/contact.html")