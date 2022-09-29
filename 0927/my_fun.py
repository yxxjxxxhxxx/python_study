# 디폴트 인자 : 파라메터의 기본 값을 설정하여 호출시
# 인자 전달 생략 가능
def test(a:str='gg', b:int=0, c:int=0 )->int: # 타입에 대한 힌트
    print(a)
    print(b+c)
    return b+c

# 가변인자 : 파라메터 개수가 고정이 아님
def test2(*args): # *args: 가변인자
    print(type(args))
    print(args)
    return sum(args)

# =================================

if __name__ == '__main__':
    res = test('aaa', 1, 2)
    print(res)

    # 키워드 인자
    res = test(a='bbb', b=10, c=5)
    print(res)

    res = test()
    print(res)

    res = test('qwer')
    print(res)

    res = test('qwer', 1)
    print(res)

    res = test('qwer', 1, 2)
    print(res)

    print("가변인자")

    s = test2(1,2,3,4)
    print(s)

    s = test2(1,2,3,4,5)
    print(s)

