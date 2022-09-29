set1 = {1,2,3,4}
print(set1)
print("=====")

set2={1, 'aaa', (3,4)}
print(set2)
print("=======")
print("set은 순서가 없다.")
list1 = [6,7,8]
set5 = set(list1)
print(set5)
print("=======")

print("set 은 중복이 안된다.")
set7 = {2,5,4,5,6}
print(set7)
{2, 4, 5, 6}
print("----------")
print("set 요소 추가")
set11 = set()
set11.add(1)
set11.add('asdf')
print(set11)
print("----------")
print("set 요소 여러개 추가")
set11.update([1,3,7,9])
print(set11)
print('============')
print("요소 삭제")
set11.remove(3)
print(set7)
print("remove( ) 는 값이 없으면 에러")
print("discard( ) 는 값이 없어도 ㄱㅊ")
set11.discard(9)
print(set11)
print("=========")

