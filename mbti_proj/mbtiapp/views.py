from django.shortcuts import render, redirect
from .models import User, MBTI, School, Major

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    school_list = School.objects.all()
    major_list = Major.objects.all()
    return render(request, 'main.html')
    
def select_school(request):
    school_list = School.objects.all()
    major_list = Major.objects.all()
    context = {
        'school_list' : school_list,
        'major_list' : major_list,
    }
    return render(request, 'select_school.html' ,context)

def my_school_main(request):
    return render(request, 'my_school_main.html')

def sign_up(request):
    school_list = School.objects.all()
    major_list = Major.objects.all()
    context = {
        'school_list' : school_list,
        'major_list' : major_list,
    }
    return render(request, 'sign_up.html',context)

def sign_mbti(request):
    return render(request, 'sign_mbti.html')

def result(request):
    return render(request, 'result.html')

def about_mbti(request):
    return render(request, 'about_mbti.html')

def search_user(request):
    return redirect

def create_user():
    return redirect