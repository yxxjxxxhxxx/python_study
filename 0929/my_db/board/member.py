class Member:
    def __init__(self, id='', pwd='', name='', email=''):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self):
        return self.id+' / '+self.pwd+' / '+self.name+' / '+self.email+' / '

import pymysql

class MemDao:

    def conn(self):
        return pymysql.connect(host='localhost', user='root', password='1234', db='python', charset='utf8')

    def insert(self, m:Member):
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'insert into member values(%s, %s, %s, %s)'
        d = (m.id, m.pwd, m.name, m.email)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def select(self, id:str)->Member:
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'select * from member where id=%s'
        cursor.execute(sql, id)
        row = cursor.fetchone() #커서에서 한줄만 추출
        conn.close()
        if row:
            return Member(row[0],row[1],row[2],row[3])

    def update(self, m:Member):
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'update member set pwd=%s, email=%s where id=%s'
        d = (m.pwd, m.email, m.id)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def delete(self, id:str):
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'delete from member where id=%s'
        cursor.execute(sql, id)
        conn.commit()
        conn.close()

class MemService:
    login_id='' #로그인 아이디

    def __init__(self):
        self.dao = MemDao()

    #id 중복체크
    def id_check(self, id:str)->bool:
        m:Member = self.dao.select(id)
        return m==None  #중복안되면 True, 아니면 False반환

    def join(self):
        print('회원가입')
        f = False
        while not f:#중복안된 id입력하면 루프 빠져나옴
            id = input('id:')
            f = self.id_check(id)
        pwd = input('pwd')
        name = input('name')
        email = input('email')
        self.dao.insert(Member(id, pwd, name, email))

    def login(self):
        print('로그인')
        id = input('id')
        pwd = input('pwd')
        m:Member = self.dao.select(id)
        if m==None:
            print('없는 아이디')
            return

        if m.pwd == pwd:
            print('로그인 성공')
            MemService.login_id = id
        else:
            print('패스워드 실패')

    def logout(self):
        MemService.login_id = ''

