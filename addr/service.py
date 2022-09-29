from addr.vo import Member
from addr.dao import Dao

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
