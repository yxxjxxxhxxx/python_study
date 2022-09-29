class PocketMon:
    def __init__(self, name='', hp=0, exp=0, lv=1):
        self.name = name    #캐릭터 이름
        self.hp = hp        #생명
        self.exp = exp      #경험치
        self.lv = lv        #레벨

    def eat(self):
        print(self.name, '밥먹음')

    def sleep(self):
        print(self.name, '잠잠')

    def play(self)->bool:
        print(self.name, '논다')

    def exc(self)->bool:
        print(self.name, '운동함')

    def print_info(self):
        print(self.name, ' 상태')
        print('hp:', self.hp)
        print('exp:', self.exp)
        print('lv:', self.lv)

    def levelup(self):
        print('레벨체크')

class Picachu(PocketMon):
    def __init__(self):
        super().__init__(name='picachu', hp=30)
        print('피카추 생성됨')

    def eat(self):
        super().eat()
        self.hp += 5

    def sleep(self):
        super().sleep()
        self.hp += 10

    def play(self) -> bool:
        super().play()
        self.hp -= 3
        self.exp += 5
        self.levelup()
        return self.hp>0

    def exc(self) -> bool:
        super().exc()
        self.hp -= 8
        self.exp += 7
        self.levelup()
        return self.hp > 0

    def levelup(self):
        super().levelup()
        if self.exp>=20:
            self.lv += 1
            self.exp -= 20
            print(self.name, '레벨 1 증가함')

    def 백만볼트(self):
        print("백만볼트 공격 ~")



#꼬부기
class Gobook(PocketMon):
    def __init__(self):
        super().__init__(name='gobook', hp=20)
        print('꼬부기 생성됨')

    def eat(self):
        super().eat()
        self.hp += 3

    def sleep(self):
        super().sleep()
        self.hp += 6

    def play(self) -> bool:
        super().play()
        self.hp -= 5
        self.exp += 8
        self.levelup()
        return self.hp > 0

    def exc(self) -> bool:
        super().exc()
        self.hp -= 7
        self.exp += 10
        self.levelup()
        return self.hp > 0

    def levelup(self):
        super().levelup()
        if self.exp >= 30:
            self.lv += 1
            self.exp -= 30
            print(self.name, '레벨 1 증가함')

    def 물대포(self):
        print('물대포 공격 ~~')

#이상해씨
class Lee(PocketMon):
    def __init__(self):
        super().__init__(name='lee', hp=10)
        print('이상해씨 생성됨')

    def eat(self):
        super().eat()
        self.hp += 15

    def sleep(self):
        super().sleep()
        self.hp += 20

    def play(self) -> bool:
        super().play()
        self.hp -= 13
        self.exp += 15
        self.levelup()
        return self.hp > 0

    def exc(self) -> bool:
        super().exc()
        self.hp -= 18
        self.exp += 17
        self.levelup()
        return self.hp > 0

    def levelup(self):
        super().levelup()
        if self.exp >= 40:
            self.lv += 1
            self.exp -= 10
            print(self.name, '레벨 1 증가함')

    def 넝쿨채찍(self):
        print('넝쿨채찍 공격 ~~')

#메뉴
class Menu:
    def __init__(self):
        self.ch = Picachu()  # 기본 캐릭터

    def select_ch(self):
        m = int(input('캐릭터 선택\n1.피카추(기본) 2.꼬부기 3.이상해씨'))
        if m==2:
            self.ch = Gobook()
        elif m==3:
            self.ch = Lee()

    def run(self):
        flag = True
        while flag:
            val = 'a'
            while not val.isdecimal(): #알파벳 입력하면 다시 입력
                val = input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료 7. 특기공격')

            m = int(val)
            if m==1:
                self.ch.eat()
            elif m==2:
                self.ch.sleep()
            elif m==3:
                flag = self.ch.play()
            elif m==4:
                flag = self.ch.exc()
            elif m==5:
                self.ch.print_info()
            elif m==6:
                break
            elif m==7:
                if isinstance(self.ch, Picachu):
                    self.ch.백만볼트()
                elif isinstance(self.ch, Gobook):
                    self.ch.물대포()
                elif isinstance(self.ch, Lee):
                    self.ch.넝쿨채찍()


        if not flag:
            print('캐릭터 사망')

if __name__=='__main__':
    m = Menu()
    m.select_ch()
    m.run()