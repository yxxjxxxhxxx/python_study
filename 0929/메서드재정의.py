# 메서드 재정의 : 상속받은 메서드를 하위 클래스에서 수정하여 사용

class Point2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_points(self):
        print('(',self.x,',',self.y,')')

class Point3(Point2):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    # 메서드 재정의
    def print_points(self):
        super().print_points()
        print('z:', self.z)

if __name__=='__main__':
    p = Point3(1,2,3)
    p.print_points()
    