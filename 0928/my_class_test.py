class Bionic:
    def __init__(self, name='', hp=50, a=10, s=5):
        self.name = name
        self.hp = hp
        self.a = a
        self.s = s

    def make_unit(self):
        print('name:', self.name)
        print('hp:', self.hp)
        print('a:', self.a)
        print('s:', self.s)

class Mechanic:
    def __init__(self, name='', hp=180, a=80, s=8):
        self.name = name
        self.hp = hp
        self.a = a
        self.s = s

    def make_unit(self):
        print('name:', self.name)
        print('hp:', self.hp)
        print('a:', self.a)
        print('s:', self.s)

if __name__=='__main__':
    m1 = Bionic(name="marian")
    m1.make_unit()

    t1 = Mechanic(name="tank1")
    t1.make_unit()

    t2 = Mechanic(name="tank2")
    t2.make_unit()

