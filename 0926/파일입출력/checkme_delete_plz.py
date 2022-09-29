total = [] # 전체 그릇
check_list = ['국', '수', '영','총점'] # 사용자에게 편하게 보여주려고 만든 리스트
# 그다음 새로운 그릇을 만들어서 total 에 넣어야함
for i in range(2): # 두명 돌리려구
    data_dish = [0,0,0,0] # 국 수 영 총
    for j in range(3): # 국 수 영 점수 돌릴라고
        data_dish[j] = int(input(check_list[j] + "어 점수:"))
        data_dish[3] += data_dish[j]
    total.append(data_dish)
    print("="*20,"끝","="*20)
print(total)








