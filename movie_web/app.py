import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from movie import Movie, MvService, DaumMvService

# flask 객체 생성. 웹 앱 객체 생성
app = Flask(__name__)
service = MvService()
dservice = DaumMvService()

@app.route('/')
def root():
    cols, data = service.get_all() #전체검색
    return render_template('index.html', cols=cols, data=data, enumerate=enumerate)

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        name = request.form['name'] #폼파라메터 속성
    else:
        name = request.args['name'] #get 방식 url 파람
    mv:Movie = service.get_by_name(name)
    return render_template('search.html', mv=mv)

@app.route('/ticket-rate')
def rate():
    # 생성될 이미지 경로
    img_path = 'static/piegraph.png'
    val = service.get_ticket_rate()
    labels = val[:, 0]
    rate = val[:, 1]*100
    fig, ax = plt.subplots()# 그래프 그릴 플랏 생성
    ex = (0.1, 0.1, 0, 0, 0)
    # matplot에서 한글 깨짐 방지
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    plt.pie(rate, labels=labels, autopct='%.1f%%', counterclock=False,
            startangle=90, explode=ex)
    fig.savefig(img_path)
    img_path = '/'+img_path
    return render_template('rate.html', val=val, img_path=img_path)

@app.route('/graph')  # 요청 url 등록
def graph():
    img_path = 'static/my_plot.png'

    x = [1, 2, 3, 4]
    y = [3, 8, 5, 6]
    fig, ax = plt.subplots()  # 그래프 그릴 플랏 생성
    plt.plot(x, y)
    fig.savefig(img_path)# 플랏의 이미지를 파일로 저장
    img_path = '/' + img_path
    return render_template('graph.html', img_path=img_path)

@app.route('/daum-rate')
def daum_rate():
    res = dservice.read_mv()
    return render_template('daum_mv.html', res=res)

if __name__=='__main__':
    app.run() # 플라스크 앱 실행