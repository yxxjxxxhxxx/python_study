# 메딕 상속 !
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp



class attack_unit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} 유닛이 {} 방향으로 공격 공격력 {}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} 유닛이 {} 대미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} 유닛의 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} 유닛 파괴".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = attack_unit("파이어뱃", 50, 15)
firebat1.attack("5시")
# 공격 두번
firebat1.damaged(25)
firebat1.damaged(25)

