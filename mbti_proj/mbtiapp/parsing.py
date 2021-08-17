from mbtiapp.models import School
import json

# with를 이용해 파일을 연다.
# json 파일은 같은 폴더에 있다고 가정!
file_path = "schooldata.json"
data = []

with open('schoolinfo.json', encoding='UTF8') as json_file:
    json_data = json.load(json_file)

    # key가 SCHOOL_NM 문자열 가져오기
    for i in range(433):
        school_name = json_data['dataSearch']['content'][i]['schoolName']
        data.append(school_name)

for item in data:
    school_obj = School(school=item)
    school_obj.save()

