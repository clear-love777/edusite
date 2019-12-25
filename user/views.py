from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def reg_view(request):
    if request.method=='GET':
        return render(request,'index/register.html')
    elif request.method=='POST':
        return render(request,'')

def login_view(request):
    return render(request,'index/index.html')