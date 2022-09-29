import json
from shlex import join

'''
# 객체 1개 json
data = '{"num": 1, "name": "aaa"}'
jsonObject = json.loads(data) # string json data parsing
print(jsonObject.get("num")) # get( ) 함수로 키값 읽음
print(jsonObject.get("name")) # 딕셔너리 키 읽기

data = '[{"num":1, "name": "aaa"}, {"num":2, "name":"bbb"}, {"num":3, "name": "ccc"}]'
jsonArray = json.loads(data)  #string json data parsing
for i in jsonArray:
    print(jsonObject.get("num"))
    print(jsonObject.get("name"))
'''
# 파일 오픈
file = open('data.json') # 파일 오픈 하는 함수
jsonData = json.load(file) # 파일에서 로드한 데이터를 파싱
print("====================================================================================================")
print(jsonData)
print("====================================================================================================")
print("====================================================================================================")
print("====================================================================================================")
print("====================================================================================================")
#for key in jsonData:
#    print(key,":", jsonData[key]) # 키와 값 출력

#print(jsonData['id']) #2728764
#print(jsonData['metadata']['width'])
#print(jsonData['metadata']['height'])
#print(jsonData['frames'])
#obj = jsonData['metadata']


#for key in obj:
#    print(key, obj.get(key))

# fbj = jsonData['frames']
# for key in fbj:
#     print(key, fbj.get(key))

'''
frames 데이터에서 다음 정보만 출력
numbers
image
위치(x,y)
카테고리 코드
'''
#arr = jsonData['frames']
#for fr in arr:
#   print('number:', fr['number'])
#   print('image:', fr['image'])
#   anns = fr['annotations']
#   for a in anns:
#      print('x:', a['label']['x'])
 #     print('y:', a['label']['y'])
 #     print('category code:', a['category']['code'])