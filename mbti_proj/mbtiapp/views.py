from django.shortcuts import render, redirect, get_object_or_404
from .models import User, MBTI, School
import json
import os #FileNotFoundError: [Errno 2] No such file or directory: './static/json/schoolinfo.json'
from django.db.models import Count


# Create your views here.
def index(request):
    data = []
    mbti_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP","ISFP", "INFP", "INTP", "ESTP","ESFP", "ENFP", "ENTP", "ESTJ","ESFJ","ENFJ","ENTJ"]


    # for j in range(16):
    #     mbti = mbti_list[j]
    #     mbti_id = str(j)
    #     mbti_obj = MBTI(mbti_id = mbti_id , mbti = mbti)
    #     mbti_obj.save()   

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
            if campus_name == "본교" :
                campus_name = ""  
            full_name = (school_name+" "+campus_name) 
            school_obj = School(school_id = school_id, school=full_name)
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

def sign_up(request,school_id):
    if school_id is not None:
        school_obj = get_object_or_404(School, school_id=school_id)
        context = {
            'school_obj':school_obj
        }
        return render(request, 'sign_up.html',context)
    return redirect(request, 'sign_up.html')

def sign_mbti(request):
    if request.method == 'POST': 
        school_id = data['school']
        user_name = data['name']
        grade = data['grade']
        context = {
            'school_id' : school_id,
            'user_name' : user_name,
            'grade': grade,
        }
        # user_obj = User(school_id = school_id, school_name=full_name)
        # school_obj.save()
        return render(request, 'sign_mbti.html', context)
    else: 
        return render(request, 'sign_mbti.html')

def result(request):
    if request.method == 'POST': 
        school = request.POST['school']
        school_obj = School.objects.filter(school_id = school)
        school_obj = school_obj[0]
        grade = request.POST['grade']
        name = request.POST['name']
        mbti = request.POST['mbti']
        mbti_obj = MBTI.objects.filter( mbti_id = mbti)
        mbti_obj = mbti_obj[0]
        user_obj = User(school = school_obj, grade = grade, name = name, mbti=mbti_obj)
        user_obj.save()
    return create_user(request)

def about_mbti(request):
    return render(request, 'about_mbti.html')

def search_user(request):
    return redirect

def create_user(request):
    mbti = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP','ISFP', 'INFP', 'INTP', 'ESTP','ESFP', 'ENFP', 'ENTP', 'ESTJ','ESFJ','ENFJ','ENTJ']
    mbti_cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    this_mbti = 0
    mbti_list = {'ISTJ':0, 'ISFJ':0, 'INFJ':0, 'INTJ':0, 'ISTP':0,'ISFP':0, 'INFP':0, 'INTP':0, 'ESTP':0,'ESFP':0, 'ENFP':0, 'ENTP':0, 'ESTJ':0,'ESFJ':0,'ENFJ':0,'ENTJ':0}
    if request.method == 'POST': 
        if request.POST['school']:
            school_id = request.POST['school']
        
        try:
            school_obj = School.objects.get(school_id = school_id)
            users = User.objects.filter(school_id = school_id)
        except:
            pass

        if users:
            for i in users:
                # this_user= User.objects.get(school_id = school_id)
                
                # mbti_list['INTJ'] = 1 #i는 user 이름이 들어감
                mbti_count = users.values('mbti_id') #[{'mbti_id': 1}, {'mbti_id': 1}]
            
            for mbti_set in mbti_count: 
                this_mbti = mbti_set['mbti_id']
                mbti_list[mbti[this_mbti]] += 1


            for i in range(16):
                cnt = mbti_list[mbti[i]]
                mbti_list[str(mbti[i])] = cnt
                mbti_list[str(mbti[i])] =  ((cnt / len(users)) * 100)
            

        mbti_count = users.values('mbti_id') #.annotate(num_mbti=Count('mbti')).order_by('num_mbti')
        mbti_list = dict(sorted(mbti_list.items(), reverse=True, key=lambda item: item[1])) 

            #dictionary 내림차순 정렬 - top 5 뽑아내려고
        data = { 
            'school_obj':school_obj,
            'users' : len(users),
            'mbti' : mbti_list.keys,
            'mbti_count' : mbti_count, #<QuerySet [{'mbti_id': 7}, {'mbti_id': 4}]>
            'mbti_list' : mbti_list, 
            'mbti_cnt' : mbti_cnt, #[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
            'range': range(16),
        }

        return my_school_main(request, data)
    else:
        school_list = School.objects.all()
        data = {
            'school_list' : school_list,
        }
        return render(request, 'select_school.html', data)