list = []
ctn = 0

def 주소등록():

    global ctn
    global list

    ctn += 1
    user = [ctn]
    user.append(input('이름을 입력해주세요 : '))
    user.append(input('휴대폰 번호를 입력해주세요 : '))
    user.append(input('주소를 입력해주세요 : '))
    list.append(user)

def 번호로_검색(num):
    for i in list:
        if num in i:
            return i
    return None

def 이름으로_검색(name):
    for i in list:
        if name in i:
            print(i)

def 수정(num):
    global list
    for i in list:
        if num in i: # 만약 i 배열에 내가 입력한 num 숫자가 있으면
            new_phone = input('수정할 전화번호를 입력해주세요 : ') # 입ㄹㄱ
            new_address = input('수정할 주소를 입력해주세요 : ') # 입력
            location = list.index(i) # 지금 찾아진 인덱스 번호를 location 에 넣는다.
            i[2] = new_phone
            i[3] = new_address
            list[location] = i
            print(list[location])

def 삭제(num):
    global list
    for i in list:
        if num in i:
            del list[list.index(i)]

def 전체목록():
    global list
    for i in list:
        print(i)

while True:
    print('1. 주소등록 , 2. 번호로 검색 3. 이름으로 검색, 4. 수정, 5. 삭제, 6. 전체목록, 7. 종료')
    put = int(input('입력해주세요 : '))
    if put == 1:
        주소등록()
    elif put == 2:
        result = 번호로_검색(int(input('번호를 입력해주세요 : ')))
        if result == None:
            print('없는 번호입니다')
        else:
            print(result)
    elif put == 3:
        이름으로_검색(input('이름을 입력해주세요 : '))
    elif put == 4:
        수정(int(input('수정할 번호를 입력해주세요 : ')))
    elif put == 5:
        삭제(int(input('삭제할 번호를 입력해주세요 : ')))
    elif put == 6:
        전체목록()
    else:
        break