#========================
print("재귀함수 팩토리얼")

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    result = factorial(5)
    print("result:", result)

main()
print()
#=========================
print('#==========================')
print()

print("피보나치 수열 - 재귀함수")
def fibo(num):
    if num==1 or num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

def main():
    for i in range(1, 51):
        print(fibo(i), end=', ')
    print()

main()

#=========================
print('#==========================')
print()
print("피보나치 수열 - 루프/리스트")


def fibo2(num):
    '''루프를 이용한 피보나치 수열'''
    n1, n2, n3 = 1, 1, 0

    for i in range(0, num):
        if i < 2:
            print(1, end=', ')
        else:
            n3 = n1 + n2
            print(n3, end=', ')
            n1 = n2
            n2 = n3
    print()


def fibo3(num):
    '''리스트를 이용한 피보나치 수열'''
    nums = [0] * num
    for i in range(0, len(nums)):
        if i < 2:
            nums[i] = 1
        else:
            nums[i] = nums[i - 1] + nums[i - 2]

    for i in nums:
        print(i, end=', ')

    print()


def main():
    fibo2(50)
    print('------------------------')
    fibo3(50)


main()
