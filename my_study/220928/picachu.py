#def 함수명 (파라메타):
# 피카츄 키우기
pica = "피카츄"
hp = 50
exp = 0
lv = 0

def 밥먹기():
    global hp
    global exp
    global pica
    global lv
    print("{} 밥먹음".format(pica))
    hp += 5
    exp += 2
    레벨업()

def 레벨업():
    global hp
    global exp
    global pica
    global lv
    if exp%20 == 0:
        lv += 1
        print("레벨업 !")

def 잠자기():
    global hp
    global exp
    global pica
    global lv
    print("{} 잠자는중 Zzz..".format(pica))
    hp += 10
    exp += 2
    레벨업()

def 운동하기():
    global hp
    global exp
    global pica
    global lv
    print("{} 운동중 으쌰으쌰".format(pica))
    hp -= 5
    exp += 2
    레벨업()
    return hp > 0

def 피카츄정보():
    print('hp: ', hp)
    print('exp: ', exp)
    print('lv: ', lv)

#main
if __name__=='__main__':
    #메뉴 1. 밥먹기 2. 잠자기
    flag = True
    while flag:
        피카츄정보()
        menu = int(input(" #메뉴 1. 밥먹기 2. 잠자기 3. 운동하기 4. 종료"))
        if menu==1:
            밥먹기()
        elif menu==2:
            잠자기()
        elif menu==3:
            flag=운동하기()
        elif menu==4:
            break
        elif hp <=0:
            print("피카츄사망")
    print('게임종료')


