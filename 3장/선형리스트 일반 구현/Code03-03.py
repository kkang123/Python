katok = ["다현", "정연", "쯔위", "사나", "지효"]

def delete_data(position):

    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    KLen = len(katok) #배열의 현재 크기
    katok[position] = None #데이터 삭제

    for i in range(position + 1, KLen): 
        katok[i - 1] = katok[i]
        katok[i] = None #배열 맨 마지막 위치 삭제

    del(katok[KLen - 1])

print(katok)
delete_data(1) #정연 삭제
print(katok)
delete_data(3) #지효 삭제
print(katok)