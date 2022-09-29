# 2일차
print(list())
range(5) # 시작값 생략/디폴트:0, 끝값:4
range(1, 5) # 시작값:1, 끝값:4
range(1, 5, 2) # 시작값:1, 끝값:4, 간격:2
# 간격 1 3 5 7


# 무한히 키보드 입력 /stop 하면 입력 종료
# 입력 문장에 금지어를 찾아서 모두 삐리리로 변환
# 금지어 목록
# 내꺼
bad_word=['십장생', '시베리아', '허스키']
# while True:
#     chat = input("채팅을 입력하세요. 채팅을 멈추고 싶다면 /stop 을 입력하세요.")
#     if chat == "/stop":
#         break
# for i in bad_word:
#     chat =
#===================================================
# 강사님꺼
data = ''
while True:
    s = input("입력문자열. /stop 은 종료")
    if s=='/stop':
        break
    data += s+'\n'
    for i in bad_word:
        data = data.replace(i, '삐리리')
    print(data)
#=============================================================
print(data)

# for i in bad_word:
#     data = data.replace(i, '삐리리')
# print(data)
#==============================================================
# 정일이꺼
# 금지어 등록
# bad_word = ['십장생', '시베리안']
#
# while True:
#     strrr = input("입력해주세요 종료하려면 /stop을 입력해주세요 : ")
#     if strrr == '/stop':
#         break
#     for i in bad_word:
#         strrr = strrr.replace(i, '*' * len(i))
#     print(strrr)
# ============================================================
