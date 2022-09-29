def add_int(a, b):
    if not isinstance(a, int):
        raise TypeError("int 타입만 연산 가능")

    if not isinstance(b, int):
        raise TypeError("int 타입만 연산 가능")

    return a + b


def main():
    try:
        result = add_int(2, 4)
        print("result:", result)

        result = add_int("2", "4")
        print("result:", result)

    except TypeError as e:
        print(e)

    except:
        print("예상치 못한 예외 발생")


main()