import random

## 전역변수 선언
totalLotto = [] # 여러 회의 추첨 번호를 모두 저장할 2차원 배열
lotto = [] #한 회의 추첨 번호 저장할 1차원 배열
pickNum = 0 # 뽑은 숫자 1개
count = 0 # 몇 회를 뽑을지 입력받는 변수

# 메인 코드
print("-- 로또 번호 생성을 시작합니다. --")
count = int(input("몇 번 뽑을까요?")) # 몇 회 추첨할지 입력 받는다.

for _ in range(count): # 입력받은(count) 만큼 추첨하기
    lotto = [] #각 회의 로또 번호 초기화
    while True:
        pickNum = random.randint(1, 45)
        if pickNum not in lotto:
            lotto.append(pickNum)
        if len(lotto) >= 6: #중복되지 않게 6개 이상이 될 때까지 무한 반복
            break
    totalLotto.append(lotto) #추첨한 숫자가 더 이상 중복되지 않으면 totallLotto에 추가
    
for lotto in totalLotto:
    lotto.sort()
    print("자동번호 -->", end = ' ')
    for i in  range(0, 6):
        print("%2d" % lotto[i], end = ' ')
    print()