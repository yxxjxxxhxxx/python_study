# vo. 한사람 정보 저장
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

class Dao:
    def __init__(self):
        # 저장할 리스트
        self.data = []

    # 리스트에 Member 객체 하나 추가
    def insert(self, m:Member):
        self.data.append(m) # 리스트 끝에 추가

    # 번호로 검색
    def select(self, num:int):
        for m in self.data:
            if m.num == num:
                return m

    # 이름으로 검색
    def select_by_name(self, name:str): # 이름 중복 허용
        res = [] # 동일한 이름 여러개
        for m in self.data:
            if m.name == name:
                res.append(m) # 이름이 같은 객체 찾으면 res에 추가
        return res

    # 삭제
    def delete(self, num:int):
        m = self.select(num)
        if m!=None:
            self.data.remove(m) # list의 remove()로 삭제. 동일한 객체를 찾아서 삭제
        else:
            print("없는번호")

class Service:
    def __init__(self, dao:Dao):
        self.dao = dao

    #추가
    def add(self):
        #정보입력
        name = input('name')
        tel = input('tel')
        addr = input('addr')

        #멤버객체 insert
        self.dao.insert(Member(name=name, tel=tel, address=addr))

    #번호로 검색
    def get_by_num(self):
        num = int(input("검색할 번호:"))
        m:Member = self.dao.select(num)
        if m == None:
            print("없는 번호")
        else:
            print(m)

    #이름으로 검색
    def get_by_name(self):
        name = input('name:')
        m:list = self.dao.select_by_name(name)
        if len(m)==0:
            print('동일한 이름 없음')
        else:
            for i in m:
                print(i)


    #수정
    def edit(self):
        num = int(input("수정할 번호:"))
        m: Member = self.dao.select(num)
        if m == None:
            print("없는 번호")
        else:
            m.tel = input('new tel:')
            m.address = input('new address:')

    #삭제
    def del_member(self):
        num = int(input("삭제할 번호:"))
        self.dao.delete(num)

    #전체출력
    def print_all(self):
        data = self.dao.data
        for m in data:
            print(m)

class Menu:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            mm = int(input('1.추가 2.번호로검색 3.이름검색 4.수정 5.삭제 6.전체목록 7.종료'))
            if mm==1:
                self.service.add()
            elif mm==2:
                self.service.get_by_num()
            elif mm==3:
                self.service.get_by_name()
            elif mm==4:
                self.service.edit()
            elif mm==5:
                self.service.del_member()
            elif mm==6:
                self.service.print_all()
            elif mm==7:
                break

if __name__=='__main__':
    m = Menu(Service(Dao()))
    m.run()
