class Test4:
    ''' class Test4'''

    cnt = 0

    def __init__(s, x, y):
        s.x = x
        s.y = y

    def printMember(s):
        print('cnt:', Test4.cnt)
        print('x:', s.x)
        print('y:', s.y)


def main():
    t = Test4(1, 2)
    print('doc:', Test4.__doc__)
    print('name:', Test4.__name__)
    print('module:', Test4.__module__)
    print('bases:', Test4.__bases__)
    print('dict:', Test4.__dict__)


main()