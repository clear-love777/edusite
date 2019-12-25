from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def teacher_index_view(request):
    return render(request,"teacher/teacher_index.html")

def teacher_course_view(request):
    id_str = request.GET.get('id','')
    if not id_str:
        return HttpResponse('课程id有误')
    id = int(id_str)
    return render(request, "teacher/teacher_course.html", locals())

def course_index_view(request):
    return render(request,"teacher/course_index.html",locals())

def course_add_view(request):
    if request.method == "GET":
        return render(request,"teacher/course_add.html")
    if request.method =="POST":
        course_name = request.POST.get("course_name")
        return HttpResponse("add ok %s"%course_name)