'''
r : 일기. 파읽없다 에러
read() 읽기 작업
w : 쓰기. 파일이 없으면 생성해서 오픈. 파일이 있으면
내용을 싹 지우고 오픈
a : 이어쓰기
write() 로 쓰기 작업
'''


'''
f=open("함수객체.py", 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()
'''
print("--------------------------------")

# f=open('함수객체.py', 'r', encoding='utf-8')
# while True:
#     line = f.readline() #한줄씩 읽기
#     if line=='': # 읽을 내용 없으면 break
#         break
#     print(line)
# f.close()
# print("====================================")
#
# f = open('c.txt', 'w', encoding='utf-8')
# while True:
#     msg = input('내용입력(멈추려면 / stop 입력)')
#     if msg == '/stop':
#         break
#     f.write(msg+'\n')
# f.close()


'''
print("========파일 복사 =============")
#파일복사

def main():
    f_name1=input('원본 파일명:')
    name = f_name1.split('.')
    f_name2 = name[0]+'_복사본.'+name[1]
    f1 = open(f_name1, 'r', encoding='utf-8')
    f2 = open(f_name2, 'w')
    str1 = f1.read()
    f2.write(str1)
    f1.close()
    f2.close()

main()
'''

'''

f = open('c.txt', 'w', encoding='utf-8')
f.write('새로운 입력내용. 이전 파일 내용은 모두삭제됨')
f.close()

'''

'''
print("a")
f = open('c.txt', 'a', encoding='utf-8')
f.write('여기서부터는 추가된 내용 \n')
f.write('블라블발브라으밟ㅇ')
f.close()
'''

f = open('c.txt', 'rb') # rb 바이너리 위치 찾으려고
s = f.read(4) # 4바이트
print(s)
print('현재위치:', f.tell()) # 현재 커서 위치 함수 tell()
f.seek(5, 1) # 몇칸 칸을 이동할지 whence 기준
print('현재위치:', f.tell())
ch = f.read(1)
print('ch:', ch)

