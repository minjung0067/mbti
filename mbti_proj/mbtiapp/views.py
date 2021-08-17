from django.shortcuts import render, redirect
from .models import User, MBTI, School, Major
import json
import os #FileNotFoundError: [Errno 2] No such file or directory: './static/json/schoolinfo.json'

# Create your views here.
def index(request):
    data = []
    full_name = ""
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'schoolinfo.json')
    with open(file_path, 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)

        # key가 SCHOOL_NM 문자열 가져오기
        for i in range(433):
            school_id = str(i)
            school_name = json_data['dataSearch']['content'][i]['schoolName']
            campus_name = json_data['dataSearch']['content'][i]['campusName']  
            full_name = (school_name+" "+campus_name) 
            school_obj = School(school_id = school_id, school_name=full_name)
            school_obj.save()

    return render(request, 'index.html')

def main(request):
    school_list = School.objects.all()
    return render(request, 'main.html')
    
def select_school(request):
    school_list = School.objects.all()
    context = {
        'school_list' : school_list,
    }
    return render(request, 'select_school.html' ,context)

def my_school_main(request, data):
    # 계산하는 부분 
    return render(request, 'my_school_main.html', data)

def sign_up(request):
    school_list = School.objects.all()
    context = {
        'school_list' : school_list,
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

def create_user(request):
    if request.method == 'POST': 
        school = request.POST['school']
        users = User.objects.filter(school = school)
        data = { 
            'school': school,
            'users' : users
        }
        return my_school_main(request, data)
    else:
        school_list = School.objects.all()
        context = {
            'school_list' : school_list,
        }
        return render(request, 'select_school.html', context)