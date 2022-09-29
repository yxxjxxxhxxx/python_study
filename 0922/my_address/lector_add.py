addr = []
cnt = 1

#새 주소 등록
def add_addr():
    global cnt
    # 한사람 정보 담을 리스트
    member = []
    member.append(cnt) # 번호 자동 할당
    cnt+=1
    member.append(input('name:')) #이름입력
    member.append(input('tel:')) #전화입력
    member.append(input('address:')) #주소입력
    addr.append(member)


# 전체 목록 출력을 도와주는 함수
def print_mem(mem):
    for data in mem:  # member에서 번호,이름,전화,주소 하나씩 꺼냄
        print(data, end=' / ')  # 꺼낸 데이터 출력
    print()

# 전체 목록 출력
def print_all():
    for mem in addr:#요소(member)를 하나씩 추출
        print_mem(mem)


#번호로 검색
def search_by_num(num): # 검색할 번호 파람
    for mem in addr: #addr에서 한명씩 꺼내서
        if mem[0]==num: #각 사람의 번호와 num이 같으면
            return mem #그 사람 리스트 반환(참조값)

#이름으로 검색
def search_by_name(name):
    res = [] #이름 같은 사람들 담을 리스트
    for mem in addr: #addr에서 요소(mem) 하나씩 꺼냄
        if mem[1]==name: #mem에서 이름이 같은 요소 찾으면
            res.append(mem)  #res에 담음
    return res #검색 결과가 담긴 res반환

#번호로 검색하여 출력
def print_by_num():
    num = int(input('검색할 사람의 번호:'))
    mem = search_by_num(num)
    if mem==None:
        print('없는 번호')
    else:
        print_mem(mem)

#이름으로 검색하여 출력
def print_by_name():
    name = input('검색할 사람의 이름:')
    mems = search_by_name(name)
    if len(mems)==0:
        print('없는 이름')
    else:
        for mem in mems:
            print_mem(mem)

def edit_addr():
    num = int(input('수정할 사람의 번호:'))
    mem = search_by_num(num)
    if mem==None:
        print('없는 번호')
    else:
        mem[2]=input('new tel:')    #요소의 전화번호 수정
        mem[3]=input('new addr:')    #요소의 주소 수정

def del_addr():
    num = int(input('삭제할 사람의 번호:'))
    mem = search_by_num(num)
    if mem == None:
        print('없는 번호')
    else:
        addr.remove(mem)    # 요소 삭제

if __name__=='__main__':
    while True:
        m = input('1.등록 2.번호로검색 3.이름으로검색 4.수정 5.삭제 6.전체출력 7.종료')
        if m=='1':
            add_addr()
        elif m=='2':
            print_by_num()
        elif m=='3':
            print_by_name()
        elif m=='4':
            edit_addr()
        elif m=='5':
            del_addr()
        elif m=='6':
            print_all()
        elif m=='7':
            break