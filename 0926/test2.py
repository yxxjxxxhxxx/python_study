#def 함수명 (파라메터...):
#    실행문

hp = 30  #생명 0이 되면 죽음
exp = 0  #경험치
lv = 1   #레벨
def 밥먹기():
    global hp #global: 전역변수 끌어다 사용
    print("피카츄 밥먹음")
    hp += 5

밥먹기() #함수 호출
print(hp)
밥먹기()
밥먹기()
밥먹기()
print(hp)

# def 잠자기(): # hp 10 증가
#     global hp
#     hp += 10
#     return hp
#
# def 놀기(): # hp 4감소, exp 5 증가, 살았나 죽었나 체크
#     global hp, exp
#     hp -= 4
#     exp += 5
#     if hp < 0:
#         print("피카추 wasted")
#     else:
#         print("피카피카")
#     return hp
#
# def 운동(): # hp 8감소, ex 12 증가, 살았나 죽었나 체크
#     global hp, exp
#     hp -= 8
#     exp += 12
#     if hp <0:
#         print("피카추 wasted")
#     else:
#         print("피카피카~")
#     return hp, exp
#
# def 레벨업(): #레벨업: ex 20마다 레벨 1증가
#     global exp, lv
#     if exp == 20:
#         lv += 1
#         exp = 0
#     return exp, lv

def 잠자기():
    global hp
    print("피카추 잠")
    hp += 10

def 놀기(): #hp 4감소, exp 5 증가, 살았나 죽었나 체크
    global hp,exp
    print("피카쵸 논다 ㅋ")
    hp -= 4
    exp += 5
    레벨업() # 경험치가 올라가므로 레벨체크
    return hp > 0 # 살았나 죽었나 반환

def 운동(): # hp 8감소, exp 12증가, 살았나 죽었나 체크
    global hp, exp
    print("피카추 운동중 ㅋ")
    hp -= 8
    exp += 12
    레벨업() # 경험치가 올라가므로 레벨체크
    return hp > 0 # 살았나 죽었나 반환

def 레벨업(): # 레벨업: exp 20마다 레벨 1증가
    global lv, exp
    if exp >= 20:
        print('레벨이 1 증가함')
        lv += 1
        exp -= 20

def printInfo():
    print('hp:', hp)
    print('exp', exp)
    print('lv:', lv)






#main
if __name__=='__main__':
    #메뉴:1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료
    flag = True
    while flag:
        printInfo()
        menu = int(input('메뉴: 1밥먹기 2잠자기 3놀기 4운동하기 5상태확인 6종료'))
        if menu==1:
            밥먹기()
        elif menu==2:
            잠자기()
        elif menu==3:
            flag=놀기()
        elif menu==4:
            flag=운동()
        elif menu==5:
            printInfo()
        elif menu==6:
            break
        elif hp <= 0:
            print("피카츄 사망")
    if hp<0:
        print('캐릭터 사망')

    print('게임종료')














