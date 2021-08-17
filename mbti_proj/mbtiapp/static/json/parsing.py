import json

# with를 이용해 파일을 연다.
# json 파일은 같은 폴더에 있다고 가정!

with open('schoolinfo.json','rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)

    # 문자열
    # key가 json_string인 문자열 가져오기
    json_string = json_data["SCHOOL_NM"]
    print(json_string);

