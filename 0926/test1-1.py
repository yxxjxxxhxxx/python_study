#range(start, end, step=1):연속된 숫자 나열을 만들어줌
a = list(range(1, 11))
print(a)
b = list(range(1, 11, 2))
print(b)

for i in range(1, 101, 2):
    print(i)

s=0
for i in range(1, 101):
    s+=i
print(s)

for i in [1,2,3,4,5]:
    print(i, end=', ')
print()

for i in range(1, 10):
    print('3 *',i,'= ', 3*i)

for i in range(2, 10):
    for j in range(1, 10):
        print(i,'*',j,'= ', i*j)

for i in range(1, 10):
    for j in range(2, 10):
        print(j,'*',i,'= ', i*j, end='\t\t')
    print()

#학점 출력
#잘못된 점수(score<0 or score>100) 입력하면 다시 입력받음

score = -1
while score < 0 or score > 100:
    score = int(input('score:'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="\t\t")
