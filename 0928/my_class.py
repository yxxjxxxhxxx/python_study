# 번호, 이름 , 전화, 주소
# 클래스 정의
class Test:
    val=3 # 클래스 레벨 변수. 객체 생성과 상관없이 사용
    #생성자
    #모든 메서드의 첫 파라메터는 객체 참조값(this)(self)
    def __init__(self, name='', age=0):
        # 멤버 변수 정의
        # self.이름 => 멤버변수
        self.name = name
        self.age = age
        self.__y = 10 #private 멤버
        # self.Y = self.__y

    def print(self):
        #self.x = 10 # 생성자가 아닌 메서드에서 멤버변수를 만들 수 있따.
        print('name:', self.name)
        print('age:', self.age)
        print('__y:', self.__y)

        # 클래스 레벨 메서드(정적메서드)
    def method():
        print('정적 메서드')
        print(Test.val)

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y


if __name__=='__main__':

    print(Test.val) # val은 정적 변수 이므로 객체 생성 없이 사용 가능
    Test.method()

    t1 = Test()
    t1.print()
    print('t1.name:', t1.name)  # name: public
    print('t1.age:', t1.age)    # age:public
    print('t1.__y:', t1.getY()) # __y:private

    t2 = Test(name='aaa')
    t2.print()

    t3=Test(name='bbb', age=45)
    t3.print()

    data = []
    data.append(Test('ddd',23))
    data.append(Test('ccc', 12))
    for obj in data:
        obj.print()

