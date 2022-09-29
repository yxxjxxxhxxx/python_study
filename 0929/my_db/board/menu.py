from member import MemService

class Menu:
    def __init__(self):
        self.memservice = MemService()

    def run_mem(self):
        while True:
            m = input('1.회원가입 2.로그인 3.로그아웃 4.내정보보기 5.내정보수정 6.탈퇴 7.종료')
            if m == '1':
                self.memservice.join()
            elif m == '2':
                self.memservice.login()
            elif m == '3':
                self.memservice.logout()
            elif m == '4':
                pass
            elif m == '5':
                pass
            elif m == '6':
                pass
            elif m == '7':
                break

    def run_board(self):
        pass

    def run(self):
        while True:
            m = input('1.회원관리 2.게시판 3.종료')
            if m=='1':
                self.run_mem()
            elif m=='2':
                self.run_board()
            elif m=='3':
                break;