import requests as requests
from bs4 import BeautifulSoup


class Movie:
    def __init__(self, rank=None, mv_name=None, opendt=None, ticket_rate=None,
                 ticket_sales=None, acc_sales=None, tic_au=None, acc_au=None):
        self.rank = rank
        self.mv_name = mv_name
        self.opendt = opendt
        self.ticket_rate = ticket_rate
        self.ticket_sales = ticket_sales
        self.acc_sales = acc_sales
        self.tic_au = tic_au
        self.acc_au = acc_au

    def __str__(self):
        val = 'rank:'+self.rank+'\n'
        val += 'mv_name:' + self.mv_name + '\n'
        val += 'opendt:' + self.opendt + '\n'
        val += 'ticket_rate:' + self.ticket_rate + '\n'
        val += 'ticket_sales:' + self.ticket_sales + '\n'
        val += 'acc_sales:' + self.acc_sales + '\n'
        val += 'tic_au:' + self.tic_au + '\n'
        val += 'acc_au:' + self.acc_au + '\n'
        return val

import pandas as pd
import matplotlib.pyplot as plt

class MvService:
    '''
    1. 영화 이름으로 검색
2. 1~10위 영화 제목 출력
3. 예매 점유율로(1~5위) 파이 그래프 출력
4. 개봉일로 검색(연도-월)
    '''
    def __init__(self):
        self.df = pd.read_excel('static/영화순위.xlsx', engine='openpyxl')

    def get_by_name(self, name):
        data = self.df
        mv = data[data['영화명']==name]
        return Movie(rank=mv['순위'].values[0], mv_name=mv['영화명'].values[0], opendt=mv['개봉일'].values[0],
                     ticket_rate=mv['예매점유율'].values[0],ticket_sales=mv['예매매출액'].values[0],
                     acc_sales=mv['누적매출액'].values[0],tic_au=mv['예매관객수'].values[0], acc_au=mv['누적관객수'].values[0])

    def get_all(self):
        data = self.df.values
        cols = self.df.columns.values
        return cols, data

    def get_ticket_rate(self):
        return self.df.head()[['영화명','예매점유율']].values

class DaumMv:
    def __init__(self, src=None, title=None, score=None, rate=None, opendt=None, acc_au=None):
        self.src = src
        self.title = title
        self.score = score
        self.rate = rate
        self.opendt = opendt
        self.acc_au = acc_au

class DaumMvService:
    def read_mv(self):
        url = 'https://search.daum.net/search?w=tot&q=%EC%8B%A4%EC%8B%9C%EA%B0%84%EC%98%81%ED%99%94%EC%98%88%EB%A7%A4%EC%9C%A8&DA=MOR&rtmaxcoll=MOR'
        html = requests.get(url).text  # 웹 요청

        root = BeautifulSoup(html, 'html.parser')
        ol = root.select('#morColl > div.coll_cont > div > ol')[0]
        lis = ol.select('li')
        res = []
        for i in range(5):
            li = lis[i]
            src = li.select('div.wrap_thumb > a > img')[0]['src']
            title = li.select('div.wrap_cont.cont_type2 > div > a')[0].text
            score = li.select('div.wrap_cont.cont_type2 > dl.dl_comm.star_comp_s > dd.score > em')[0].text
            rate = li.select('div.wrap_cont.cont_type2 > dl:nth-child(3) > dd')[0].text
            opendt = li.select('div.wrap_cont.cont_type2 > dl:nth-child(4) > dd')[0].text
            acc_au = li.select('div.wrap_cont.cont_type2 > dl:nth-child(5) > dd')[0].text
            res.append(DaumMv(src=src, title=title, score=score, rate=rate, opendt=opendt, acc_au=acc_au))
        return res
