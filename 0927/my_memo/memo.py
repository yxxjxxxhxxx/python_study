import os

#==== 디렉토리 만드는 코드
def mk_dir(name):
    if not os.path.isdir(name): # 이름의 디렉토리가 없으면
        os.mkdir(name) # 디렉토리 만들기
        print(name, '디렉토리가 생성 되었음')
#======================== 디렉토리 만들기
# 한번만 생성됨

# 디렉토리 목록 선택 코드

def select_files(dname):
    files = os.listdir(dname) # 디렉토리 이름을 넣어주면 파일 목록을 보여줌
    print(files)
    for idx, f in enumerate(files): # 인덱스랑 파일명 가져와서 출력
        print(idx,'.',f) #파일 출력 했을때 번호 로 선택하기위해
    num = int(input('읽거나 삭제 하고 싶은 파일 번호를 입력'))
    if 0<=num<len(files): # ui 가 아닌 콘솔이기 때문에 이상한값을 못넣게 하기 위해
        return files[num] # num 을 1로 하면 files 리스트에 있는 memo.py 가 넘어감
# print_files('./') 하면 안에 있는 파일 목록 나옴

# 선택한 파일 읽기 코드
def read_file(dname):
    fname = select_files(dname)
    if fname==None: # 리스트의 없는 값을 입력 했을때
        print(" 잘못된 번호다")
    else: # 리스트의 있는 값을 입력하면
        path = dname+'/'+fname
        f = open(path,'r', encoding='utf-8')
        content = f.read()
        print(content)

# 파일 중복 체크 코드
def check_filename(dname):
    # 지정한 디렉토리의 파일 목록을 읽음
    flist = os.listdir(dname)
    # 쓰기할 파일명 입력
    fname = input('파일명 입력')
    # 오픈 모드 저장 (쓰기 w)
    mode = 'w'

    # fname 이 dname 에 포함이 되어 있느냐.(포함되어있으면 중복되는것 이니까)
    # 중복이 안되면 바로 fname, mode 리턴
    # 중복된 이름이면 루프를 돌음
    while fname in flist:
        m = input('중복된 파일명 1.다시입력 2.덮어쓰기 3.이어쓰기')
        if m=='1':
            fname = input('파일명 입력')
        elif m=='2':
            break
        elif m=='3':
            mode = 'a' # 이어쓰기
            break
    return fname, mode

# 파일 쓰기 코드(함수)
def write_file(dname):
    # 파일명 입력 및 중복 체크해서 겨로가를 fname, mode에 저장
    fname, mode = check_filename(dname)

    # 오픈할 파일 경로 '디렉토리명/파일명'
    path = dname+'/'+fname

    # 파일 쓰기 모드 오픈 mode 가 a 일 수도 w 일수도 사용자지정
    f = open(path, mode, encoding='utf-8')
    while True:
        content = input('파일 내용 입력. 루프 나가려면 /stop')
        if content == '/stop':
            break
        # 파일쓰기
        f.write(content+'\n')
    f.close()

def del_file(dname):
    fname = select_files(dname)
    if fname==None:
        print('잘못된 번호')
    else:
        os.remove(dname+'/'+fname)








if __name__=='__main__':
#    mk_dir('memo')              #디렉토리만들기
#    read_file('./')             #파일읽기 체크
#   print(check_filename('./'))  #중복파일 체크
    dname = 'memo'
    mk_dir(dname)
    while True:
        m = input('1.읽기 2. 쓰기 3. 삭제 4. 종료')
        if m=='1':
            read_file(dname)
        elif m=='2':
            write_file(dname)
        elif m=='3':
            del_file(dname)
        elif m=='4':
            break
