class Board:
    def __init__(self, num=0, writer='', w_date='', title='', content=''):
        self.num = num
        self.writer= writer
        self.w_date = w_date
        self.title = title
        self.content = content

    def __str__(self):
        return 'num:'+str(self.num)+' / writer:'+self.writer+' / w_date:'+self.w_date+' / title:'+self.title+' / content:'+self.content

class BoardDao:
    def conn(self):
        pass

    #글작성. 입력받은 값은 title, content만. 나머지 글번호,작성자,작성일(now())는 자동값
    def insert(self, b:Board):
        pass

    #글 번호로 검색하여 Board 객체 반환
    def select(self, num:int)->Board:
        pass

    #글 작성자로 검색하여 리스트에 담아서 반환
    def select_by_writer(self, writer:str)->list:
        pass

    #글 타이틀로 검색하여 리스트 반환(like 패턴검색)
    def select_by_title(self, title:str)->list:
        pass

    #글 수정. 글번호로 찾아서 title, content는 입력받은 값으로 수정. w_date는 현재(now())날짜로 수정
    def update(self, b:Board):
        pass

    #글삭제. 글번호로 삭제
    def delete(self, num:int):
        pass

class BoardService:
    def __init__(self):
        self.dao = BoardDao()

        # 글작성. 입력받은 값은 title, content만. 나머지 글번호,작성자,작성일(now())는 자동값
        def add(self):
            pass

        # 글 번호 입력받아 검색하여 출력
        def get_one(self):
            pass

        # 글 작성자로 검색하여 출력
        def get_by_writer(self):
            pass

        # 검색할 타이틀 입력받아 검색하여 출력
        def get_by_title(self):
            pass

        # 글 수정. 수정할 글의 번호,new title,new content는 입력받아 수정
        def edit(self):
            pass

        # 글삭제. 글번호 입력받아 삭제
        def delete(self):
            pass