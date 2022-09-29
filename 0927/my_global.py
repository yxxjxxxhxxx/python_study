a = 10  # 전역변수. 이 파일 어디에서나 사용가능한 변수. 단 사용전 선언은 필수


def f1(x):  # 파라메터도 지역변수
    b = 20  # 지역변수
    print('a:', a, 'b:', b, 'x:', x)


def f2():
    # 에러: b와 x는 f1()의 지역변수이므로 다른 함수에서 사용 불가
    print('a:', a, 'b:', b, 'x:', x)


def f3():
    a = 100  # a:지역변수
    print('f3()에서 a:', a)


def f5():
    global a  # a:전역변수
    a = 200
    print('f5()에서 a:', a)


def f4():
    print('f4()에서 a:', a)


'''
f1(30)
f2()
'''
f3()
f4()
f5()
f4()

#==============================
print("#======================")
#전역변수의 visible
def f1():
    print("f1()")
    print("a =", a)
    #print("b =", b)
    #print("c =", c)

def f2():
    print("f2()")
    print("a =", a)
    print("b =", b)
    #print("c =", c)

def f3():
    print("f3()")
    print("a =", a)
    print("b =", b)
    print("c =", c)

a = 10
f1()
b = 20
f2()
c = 30
f3()