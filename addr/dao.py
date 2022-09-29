from addr.vo import Member
# addr.vo 모듈에 있는 Member 임포트

class Dao:
    def __init__(self):
        # 저장할 리스트
        self.data = []

    # 리스트에 Member 객체 하나 추가
    def insert(self, m:Member):
        self.data.append(m) # 리스트 끝에 추가

    # 번호로 검색
    def select(self, num:int):
        for m in self.data:
            if m.num == num:
                return m

    # 이름으로 검색
    def select_by_name(self, name:str): # 이름 중복 허용
        res = [] # 동일한 이름 여러개
        for m in self.data:
            if m.name == name:
                res.append(m) # 이름이 같은 객체 찾으면 res에 추가
        return res

    # 삭제
    def delete(self, num:int):
        m = self.select(num)
        if m!=None:
            self.data.remove(m) # list의 remove()로 삭제. 동일한 객체를 찾아서 삭제
        else:
            print("없는번호")
