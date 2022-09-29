import json

class Movie:
    def __init__(self, rank=0, mvName='',opendt='', salesAmt=0, audiCnt=0):
        self.rank = rank
        self.mvName = mvName
        self.opendt = opendt
        self.salesAmt = salesAmt
        self.audiCnt = audiCnt

    def __str__(self):
        return '순위:'+str(self.rank)+'\n'+ '영화명:'+self.mvName+'\n'+ '개봉일:' + self.opendt + '\n' + '일매출:'+str(self.salesAmt)+'\n' +'누적관객수:' + str(self.audiCnt) + '\n===============\n'

class Service:
    def __init__(self, path):
        self.path = path  #json파일 경로
        self.data = []  #파싱 데이터 객체를 담을 리스트

    def read_json(self):
        f = open(self.path, 'r', encoding='utf-8')
        jdata = json.load(f)
        # infos: 리스트
        infos = jdata["boxOfficeResult"]["dailyBoxOfficeList"]
        for info in infos:
            r = int(info.get("rank"))
            m = info.get("movieNm")
            o = info.get("openDt")
            s = int(info.get("salesAmt"))
            a = int(info.get("audiCnt"))
            self.data.append(Movie(rank=r, mvName=m, opendt=o, salesAmt=s, audiCnt=a))

    def print_all(self):
        for d in self.data:
            print(d)

if __name__=='__main__':
    service = Service('searchDailyBoxOfficeList.json')
    service.read_json()
    service.print_all()