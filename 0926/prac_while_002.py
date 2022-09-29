# while
'''
1) while문
while 문은 조건을 명시하고
 그 조건이 True일 동안 반복하고,
조건이 False가 되면 루프를 빠져 나온다.
'''

# * 삼각형
print("# 삼각형 만들기")
'''
*
**
***
****
'''
z = 0
x = 1
while z<6:
    print("*" *x)
    z += 1
    x += 1

print(1%2)
print(1/2)
print(2%1)
print(2/1)


#====================================
 # 1~ 100 사이의 홀수 1번
print("# 1~ 100 사이의 홀수 1번 ")
i = 1  #
while i<=100:
    if i%2 ==1:
        print(i, end=",")
    i+=1
print("범위 종료 끝끝")
#====================================

# 1~ 100 사이의 홀수 2번
print("# 1~ 100 사이의 홀수 2번 ")

i=1
while i<=100:
    print(i, end=",")
    i+=2
print('여기는 루프 밖')

#====================================
# 1~ 100 사이의 짝수
print("# 1 ~ 100 사이의 짝수")
i = 1
while i <= 100:
    if i%2 == 0:  # != 도 됨
        print(i, end=",")
    i+=1
print("짝수 끝")
#====================================

# 100 이하의 합
print("100 이하의 합")
s = 0
i=1
while i <= 100:
    s+=i  # 위 아래를 바꾸면 s = s + 1 이 아니라
    i+=1  # s = s + 2 가 되어버려서 값이 다르다.
print("1~100까지의 합 = ", s)
#====================================

#====================================
# 구구단 한단 출력
'''
print("# 구구단 한단 출력")
s=int(input('단수를 입력하시오'))
i=1
while i<10:
    print(s, '*', i, '=', s*i)
    i+=1
'''
#====================================
### 3줄 출력
print("###을 3줄 출력")
i=1
while i<=12:        # i 가 12 보다 작거나 같을 때 까지 반복한다.
    if i%4==0:      # 만약 i 나누기 4 나머지가 0이면
        print()     # 엔터 (줄바꿈)
    else:           # i 나누기 4가 0이 아니라면
        print('#', end='')  # #을 출력 하지만 줄바꿈을 하지않고 대기
    i+=1            # 루프 돌때마다 index 값 1 증가
# 한마디로 (4의배수가 아니면) ### 을하고 4의 배수가 되면 줄바꿈을 한다.

#====================================

#====================================
### 2줄 출력(2중 루프)
print()
print("### 을 2줄 출력(2중 루프)")

i=1
while i<=2:#줄은 만든다. 2줄 만듬.
    j=1
    while j<=3:#칸을 만든다. 3칸
        print('#', end='')
        j+=1
    print()
    i+=1

i = 1
while i<=2:
    print("#", end=" ")
    j=1
    while j <=10:
        print("=", end="")
        j+=1
    print()
    i+=1

#====================================

#무한루프
print()
print("# 무한루프")
#=======참 거짓을 활용==================
# while True: #무한루프
#     print('true')

# i = 1 인데 5보다 커질수 없으므로 무한
#i=1
#while i<5:#무한루프
#    print(i)

# 왜 있는지는 모르겠으나 0번 도는 루프
#i=1
#while i>10:#0번 루프
#    print('false')
#====================================

#====================================
# 무한 루프의 활용
print("\n 무한 루프의 활용")
while True:
    a = input("메세지를 입력하세요 : 끝내고 싶으시면 /stop 을 입력하세요")
    if a == "/stop":
        break
    else:
        print("입력한 메세지는 : ", a, "입니다.")


