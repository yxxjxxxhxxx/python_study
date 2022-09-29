# 회사가면 제일 먼저 하는게 뭐해봤냐, 안했씀 ㅋ

# 제일 먼저 하는것은 초기화 해서 하는것
# 요소로 접근
l1 = [1,2,3]
for i in l1: # l1 의 요소를 하나씩 꺼내서 i에 할당하여 루프 사용
    print(i)


# 인덱스로 접근
# len 은 int를 받을 수 없다.
for i in range(0, len(l1)): #range 인덱스 값 생성(0,1,2)
    print(l1[i])

l1[2] = 30 # l1 의 2번째 인덱스를 30으로 변경
print(l1[2])
print(l1)

l1.append(4) # 끝에 방에 추가해 주고 새 방에 값 할당
print(l1)

# 빈리스트 l2 를 정의하고 숫자 5개 입력 받아 리스트 만들기
# l2 = []
# for i in range(5): # range 는 0이 default
#     a =input("값 넣으세요")
#     l2.append(a)
# print(l2)

# l3 = [[1,2,3],[4,5,6]]
# for i in l3:
#     for j in i: #i:[1,2,3]
#         print(j, end=',')
#     print()

# 2명의 국영수 값 받고 각각의 총점 출력
# 강사님꺼
# score = [] # score 리스트 만들기
# title = ['kor', 'eng', 'math', 'total'] # 타이틀 리스트에 값을 4개 넣기
# for i in range(3): # for 반복문 3번연속 해서 i는 몇번쨰 반복중이냐
#     data = [0,0,0,0] # 1명 점수 data 리스트에 0,0,0,0 를 만든다.
#     for j in range(3): #
#         data[j] = int(input(title[j] + ':')) # 국영수 값 입력
#         data[3] += data[j] # 총점에 누적
#     score.append(data) # 완성된 1명 데이터를 score 에 추가
# print(score)

#규리꺼
# 국, 영, 수 값을 입력받고 총점과 함께 출력하시오.
# x = 0
# result = []
# for i in range(3):
#     a = input().split() # 값을 띄어쓰기로 입력해야 함
#     for j in range(len(a)):
#         a[j] = int(a[j])
#         x += a[j]
#     a.append(x)
#     x = 0
#     result.append(a)
# print(result)

#정일이꺼
# for i in range(0,3):
#      hahaha = []
#      student_score = 0
#      for j in range(0,3):
#         score = int(input('국영수 값을 입력해주세요'))
#         hahaha.append(score)
#      for j in hahaha:
#          student_score += j
#
#      hahaha.append(student_score)
#      student.append(hahaha)
# print(student)
# print('A학생 총점 : ',student[0][3])
# print('B학생 총점 : ',student[1][3])
# print('C학생 총점 : ',student[2][3])
# ========================================
l4 = ['aaa', 'bbb','ccc','ddd','eee']
for idx, data in enumerate(l4): # enumerate = 세다
    print(idx,':',data)
# 리스트 슬라이싱[시작인덱스 : 끝인덱스]
print(l4[1:3]) # 1~2번방 추출
print(l4[:3]) # 맨앞방 ~ 2번방 추출
print(l4[1:]) # 1번방 ~ 끝방 추출
print(l4[1:5:2]) # 1~4번 방까지 2간격으로 데이터 추출

# 오류남 list.insert(1,5) #param1:끼워넣을 위치의 인덱스. param:추가할 값
print("89번줄 val 'abc' 시작")
val = 'aaa'
if val in l4:
    print(val, '값이 있다')
else:
    print('값이 없다')

idx = l4.index(val) #index(값) : 리스트에서 값의 위치 반환
print(idx, '방에 방에 있음')

list23 = [1,2,4,5]
list23.append(3)
list23.sort(reverse=False)
print(list23)

