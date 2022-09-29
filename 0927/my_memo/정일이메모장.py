import os

location = os.getcwd() + '\memo'

def 작성(f):
    print("파일 작성이 시작됩니다. 그만 멈추고 싶으시면 ./stop을 입력해주세요")
    while True:
        stop_or_no = input(': ')
        if stop_or_no == './stop':
            break
        f.write(stop_or_no+"\n")
    f.close()

def 메모_읽기():
    list = os.listdir(location)
    for i in list:
        print(list.index(i)+1,".",i)
    sele = int(input('읽을 메모를 번호를 입력해주세요 : '))
    if os.path.isfile(location+'\\'+list[sele-1]):
        f = open(location+'\\'+list[sele-1],'r')
        str1 = f.read()
        print(str1)
    else:
        print("없는 파일 번호입니다")
        main()

def 이어쓰기(inpp):
    f = open(location+'\\'+inpp+".txt",'a')
    작성(f)


def 덮어쓰기(inpp):
    f = open(location + '\\' + inpp + ".txt", 'w')
    작성(f)

def 쓰기():
    inpp = input("파일 명을 입력해주세요 : ")
    if os.path.isfile(location+"\\"+inpp+".txt"):
        print("파일이 이미 존재합니다")
        print("1. 이어쓰기  2. 덮어쓰기  3. 새 파일명 입력  4. 종료 ")
        inppp = input("메뉴를 입력해주세요 : ")
        if inppp == '1':
            이어쓰기(inpp)
        elif inppp == '2':
            덮어쓰기(inpp)
        elif inppp == '3':
            쓰기()
        else:
            main()
    else:
        print("파일이 새로 생성 됐습니다.")
        f = open(location+"\\"+inpp+".txt", "w+")  # w+:읽고 쓰기 모드. 파일이 없으면 새로 생성해서 오픈
        작성(f)


def 파일삭제():
    inpp = input("파일 명을 입력해주세요 : ")
    if os.path.isfile(location + "\\" + inpp + ".txt"):
        os.remove(location + "\\" + inpp + ".txt")
    else:
        print("정확한 파일 명을 입력해주세요")
        main()


def main():
    while True:

        if os.path.isdir(location):
            pass
        else:
            os.mkdir(location)

        print('1. 메모 읽기  2. 쓰기  3. 파일 삭제  4. 종료')
        inp = input("번호를 입력해주세요 : ")
        if inp == '1':
            메모_읽기()
        elif inp == '2':
            쓰기()
        elif inp == '3':
            파일삭제()
        else:
            break


main()