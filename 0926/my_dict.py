d1 = {'name' : 'aaa', 'age' :12}
print(d1['name'])
print(d1['age'])

print(d1)
d1['tel']='111' # 요소 추가 새 키로 값 할당
print(d1)

d1['name'] = 'bbb' # 요소 값 변경
print(d1)

d1.pop('tel') # 요소 삭제
print(d1)
