def main():
    list1 = [1, 2, 3]
    try:
        print(list1[1])
        result = 3 / 5
        res = 3 + 'abc'
        print("result=", result)

    except ZeroDivisionError:
        print("0으로 나눌 수 없다.")

    except IndexError:
        print("없는 인덱스에 접근")

    except Exception as e:
        print("모든 예외 처리")
        print(type(e))

    except:
        print("모든 예외 처리")

    else:
        print("예외가 발생하지 않았다.")

    finally:
        print("종료전 무조건 실행 .")

    print("프로그램은 중단되지 않는다")


main()