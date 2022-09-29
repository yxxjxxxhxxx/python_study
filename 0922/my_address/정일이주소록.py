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


def 이름으로_검색(name):
    for i in list:
        if name in i:
            print(i)

def 수정(num):
#  global list
    for i in list:
        if num in i:
            new_phone = input('수정할 전화번호를 입력해주세요 : ')
            new_address = input('수정할 주소를 입력해주세요 : ')
            location = list.index(i)
            print(location)
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

# 클론 코딩을 먼저 해라 만약 그게 되면 쿵코로콩콩쿵쿠루루룽(자신이 생각해서 직접 코드짜기)을 해라
# 강사님이 친걸 그대로 쳐봐라
# 컨시 컨브가 답이다
# Flow를 이해해라
# 매일 공부한걸 복습하며 정리해라