class Parent:
    def __init__(self, x=0):
        print('parent 생성자')
        self.x = x

    def parent_method(self):
        print('x:', self.x)

# Parent를 상속받는 Child
class Child(Parent):
    def __init__(self, x=0, y=0):
        super().__init__(x)# 부모 생성자를 호출
        print('child 생성자')
        self.y = y

    def child_method(self):
        print('x:', self.x)
        print('y:', self.y)

class Member:
    def __init__(self, name=''):
        print('member 생성자')
        self.name = name

    def print_name(self):
        print('name:', self.name)

# 클래스 다중 상속 가능. 상속할 클래스를 ,로 나열
class Test(Parent, Member):
    def __init__(self, x=0, name=''):
        Parent.__init__(self, x=x)      #부모 중 Parent의 생성자 호출
        Member.__init__(self, name=name)   #부모 중 Child의 생성자 호출
        print('Test 생성자')

    def print_info(self):
        print('x:', self.x)
        print('name:', self.name)

if __name__=='__main__':
    p = Parent(1)
    p.parent_method()

    c = Child(2, 3)
    c.parent_method()
    c.child_method()

    t = Test(x=4, name='aaa')
    t.print_info()
    t.parent_method()
    t.print_name()