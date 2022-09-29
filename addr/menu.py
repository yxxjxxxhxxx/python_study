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
