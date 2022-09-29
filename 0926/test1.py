a = 12
b = 'abcd'
print("a=", a,"type=",type(a))
print("b=", b,"type=",type(b))

# 주석
''' 긴줄 주석
야야야야야야야야
'''

#c = 1
#del c # 변수 삭제
#print(c)
int('23') # int
str(23) # string

# name = input('이름을 입력하세요')
# age = int(input('나이를 입력하세요'))
# dep = input('학과를 입력하시오')
# c = age + 5
# print('name:', name)
# print('age:', age)
# print('5년 뒤 age:', c)
# print('dept:', dep)

a = True
b = False
print("a:",a,"b:",b,"일때")

# and 연산자는 모두 True 가 아니면 False 반환
print("a and b: ", a and b)

# or 연산자는 하나라도 True 이면 True 반환
print("a or b:", a or b)

# not 연산자는 반대 값 반환
print("not a: ", not a)
print()

# 숫자가 0 이면 Fales 그 외 나머지는 True
a = 0
b = 7

print("a: ", a, )
print("b: ", b,)


# a = int(input('점수를 숫자로 입력하세여 '))
# 85 > a >= 65:
# print( B)
if a > 100:
    print("100 이하의 숫자를 적으세요")
elif a >= 90 and a <= 100:
     print("A")
elif a >= 80 and a <90:
     print("B")
elif a >= 70 and a <80:
     print("C")
elif a >= 60 and a <70:
     print("D")
elif a <60:
     print("F")

#range(start, end, step=1): 연속된 숫자 나열을 만들어줌
a = list(range(1, 11))
print(a)
b = list(range(1, 11, 2))
print(b)

for i in range(1, 101, 2):
    print(i)



print("----1,2,3,4,5 end=',' ---")
for i in [1,2,3,4,5]:
    print(i, end=',')
print()

# 구구단 3단
for i in range(1, 10):
    print('3 *',i,'= ', 3*i)

# 구구단 가로로
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*',j, '=', i*j)

for i in range(1, 10):
    for j in range(2, 10):
        print(j,'*',i,'= ', i*j, end='\t\t')
print()


# 학점 출력
# 잘못된 점수 (score < 0 or score > 100) 입력하면 다시 받음

score = -1
#while score < 0 or score > 100:
#    score = int(input('score: '))
#if score >= 90:
#    print('A')
#elif score >= 80:
#    print('B')
#elif score >= 70:
#    print('C')
#elif score >= 60:
#    print('D')
#else:
#    print('F')

print("=======파이썬 연산자========")
print("10/2 =", 10/2)
print("10%2 =", 10%2)
print("2/10 = ", 2/10)
print("2%10 = ", 2%10)


