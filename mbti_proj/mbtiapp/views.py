from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')
    
def select_school(request):
    return render(request, 'select_school.html')

def my_school_main(request):
    return render(request, 'my_school_main.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_mbti(request):
    return render(request, 'sign_mbti.html')

def result(request):
    return render(request, 'result.html')

def about_mbti(request):
    return render(request, 'about_mbti.html')