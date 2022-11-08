# 카톡 친구 자동 삽입하기

#예제 설명
#카톡 친구 이름과 카톡 횟수를 입력하면 자동으로 위치를 찾아 삽입하는 프로그램이다. 카톡 친구의 초기 정보는 ('친구이름', 연락횟수) 형식의 튜플 리스트로 구성

# 새로운 친구 `미나`와 40회를 입력하면 자동으로 자신의 순위에 해당하는 위치를 찾아 삽입한다. 동일한 연락 횟수라면 새로운 친구를 앞 순위로 지정한다.




def find_and_insert_data(friend, k_count):
    findPos = -1
    for i in range(len(katok)):
        pair = katok[i]   
        if k_count >= pair[i]:
            findPos = i
            break
    if findPos == -1:
        findPos = len(katok)

    insert_data(findPos, (friend, k_count))


def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend


katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


if __name__ == "__main__":

    while True:
        data = input("추가할 친구-->")
        count = int(input("카톡 횟수 -->"))
        find_and_insert_data(data, count)
        print(katok)
