# 함수객체 기본문법

def sayHello():
    print('hello~~')

def main():
    funcObj = sayHello  #함수 이름엔 함수 참조값이 저장됨
    funcObj()
    sayHello()

main()

#=================

# 함수 객체 활용 - 룩업 테이블
def error1():
    print('1번 에러 발생')


def error2():
    print('2번 에러 발생')


def error3():
    print('3번 에러 발생')


def error4():
    print('4번 에러 발생')


def main():
    ec = 2
    if ec == 1:
        error1()
    elif ec == 2:
        error2()
    elif ec == 3:
        error3()
    elif ec == 4:
        error4()


def main2():
    ec = 2
    f = [error1, error2, error3, error4]
    f[ec - 1]()


main2()

# 함수 객체 활용 - 핸들러 처리

# 2) 함수 객체 활용 - 핸들러 처리

def onEvent(f):
    print("핸들러가 등록되었습니다.")
    f()
    print()

def myHandler1():
    print("1번 이벤트 핸들러입니다.")

def myHandler2():
    print("2번 이벤트 핸들러입니다.")

def myHandler3():
    print("3번 이벤트 핸들러입니다.")

def main():
    onEvent(myHandler1)
    onEvent(myHandler2)
    onEvent(myHandler3)

main()