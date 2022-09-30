from member import MemService
from board import BoardService

class Menu:
    def __init__(self):
        self.memservice = MemService()
        self.boardservice = BoardService()

    # 회원쪽 메뉴
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
                self.memservice.print_member()
            elif m == '5':
                self.memservice.edit_member()
            elif m == '6':
                self.memservice.del_member()
            elif m == '7':
                break

    # 게시판 메뉴
    def run_board(self):
        pass

    # 상위 메뉴
    def run(self):
        while True:
            m = input('1.회원관리 2.게시판 3.종료')
            if m=='1':
                self.run_mem()
            elif m=='2':
                self.run_board()
            elif m=='3':
                break;