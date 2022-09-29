class JSS:
    def __init__(self):
        self.name = input("이름을 입력하세요")
        self.age = input("나이를 입력하세요")

    def show(self):
        print("나의 이름은 {}, 나이는 {} 입니다.".format(self.name, self.age))


class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input("성별 : ")

    def show(self):
        print("나의 이름은 {}, 성별은 {}자, 나이는 {} 입니다.".format(self.name, self.gender ,self.age))


a = JSS2()
a.show()
#a = JSS()


