bad_word = ['시베리아', '귤까', '십장생', '허스키']

# 이걸 밖에다 뒀더니 무한루프 되었다.
# 무한 루프를 돌리고 싶은 기능은 루프 안에
# 넣자 . chat = input("채팅을 치세요 종료하시려면 /stop 을 입력하세요")

while True:
    chat = input("채팅을 치세요 종료하시려면 /stop 을 입력하세요")
    if chat == "/stop":
        break

    for i in bad_word:
        chat = chat.replace(i, "*" * len(i))
    print(chat)



