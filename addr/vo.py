class Member:
    # 정적변수 번호를 자동 할당 하려고
    cnt = 1

    #생성자
    def __init__(self, name='', tel='',address=''):
        self.num = Member.cnt
        Member.cnt += 1
        self.name = name
        self.tel = tel
        self.address = address

    # toString(). object 클래스에 정의된 __str__() 재정의함
    def __str__(self) -> str:
        return 'num:'+str(self.num)+' / name:'+self.name+' / tel:' + self.tel+' / address:'+self.address
