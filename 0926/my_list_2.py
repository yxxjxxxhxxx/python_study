import copy

e = [1,2,[3,4,5]]
f = copy.deepcopy(e)
print("e=", e)
print("f=\n", f)

e[2][1]=300
print("e 의 리스트 2번쨰에 있는 1번 "
      "인덱스 값 3을 300으로 변경")
print("e=",e)
print("f=",f)
