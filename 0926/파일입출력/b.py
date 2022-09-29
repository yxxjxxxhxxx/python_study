'''
1~10위 영화의
순위
영화명
개봉일
누적관객수
일매출액
'''
import json

# 파일 오픈
file = open('searchDailyBoxOfficeList.json', 'rt', encoding='UTF8') # 파일 오픈 하는 함수
jsonData = json.load(file) # 파일에서 로드한 데이터를 파싱
d = jsonData['boxOfficeResult']['dailyBoxOfficeList']

for i in d:
    if int(i['rank']) <= 10:
        print("======영화 정보======")
        print('영화순위: ', i['rank'])
        print('영화이름: ', i['movieNm'])
        print('영화개봉일: ', i['openDt'])
        print('누적관객수: ', i['audiAcc'])
        print('일매출액:', i['salesAmt'])
        print("=======================\n")




