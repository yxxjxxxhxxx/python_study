# 재귀함수 : 함수 안에서 자신을 또 호출하는 구조. 동일한 작업을 반복처리시 사용.
# 단점 : 성능을 저하, 스택 오버플로우 발생 => 루프로 전환 권장

# factorial 4! 4!=4*3*2*1
def facto(num):
    if num==1:
        return 1
    else:
        return num * facto (num-1)


# 팩토리얼을 루프로 구현
def facto2(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

# 재귀함수
def fibo(num):
    if num < 3:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

def fibo2(num):
    data = [1]*num
    for i in range(2, num):
        data[i] = data[i-1]+data[i-2]
    return data




if __name__=='__main__':
    print('4!=', facto(4))
    print('4!=', facto(4))

    '''
    for i in range(1, 51):
        print(fibo(i), end=', ')
    '''

    print(fibo2(50))
