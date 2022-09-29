# 두개이상 상속 하는거
# 공중 유닛은 날기 기능도 있어야한다.
# 공중 유닛중 드랍쉽은 공격을 못한ㄷ.
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

# 드랍쉽 : 공중 유닛

#날 수 있는 기능을 가진 클래스
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, location):
        print("{} : {} 방향으로 날아갑니다. [속도{}]"
              .format(self.name, location, self.flying_speed))

#공중 공격 유닛 클래스
class flyable_attack_unit(attack_unit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attack_unit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)

valkyrie = flyable_attack_unit("발키리", 200, 5, 5)
valkyrie.fly("11시")
valkyrie.attack("10시")

