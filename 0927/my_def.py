# 구구단 출력함수
print("# 구구단 출력함수")

def gugudan(dan):
    "구구단 출력함수"
    for i in range(1,10):
        print(dan,'*',i,'=',dan*i)

def main():
    for i in range(2,10):
        print(i,'단')
        gugudan(i)
        print()

main()

#===========================================
print("=========================================")

#약수출력
print("약수 출력 함수")

def 약수(num):
    for i in range(1, num+1):
        if num % i ==0:
            print(i, end=',')
    print()

def main():
    num = int(input('num:'))
    약수(num)
main()

