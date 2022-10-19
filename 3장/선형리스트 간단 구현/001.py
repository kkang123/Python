fruit = ["바나나", "딸기", "포도", "사과", "감귤"]
print('초기 리스트 : ', fruit)

fruit.append(None) #빈칸 삽입
print("빈칸 삽입 후 리스트 : ",fruit)

fruit[5] = "배" #빈칸에 데이터 삽입
print("빈칸에 변수 삽입 후 리스트 : ",fruit)

fruit.append(None) #빈칸 삽입
print("빈칸 삽입 후 리스트 : ",fruit)


fruit[6] = fruit[5] #동일시 하기
fruit[5] = None # 빈칸으로 만들기
print("빈칸 동일 시 후 리스트 : ",fruit)

fruit[5] = fruit[4] 
fruit[4] = None 
fruit[4] = fruit[3] 
fruit[3] = None 
print("빈칸 이동 후 리스트 : ",fruit)

fruit[3] = "망고"
print("빈칸에 망고 추가 후 리스트 : ",fruit)


fruit[4] = None
print("빈칸에 사과를 None으로 변경 후 리스트 : ",fruit)
fruit[4] = fruit[5] 
fruit[5] = None 
print("빈칸에 None 이동 후 리스트 : ",fruit)
fruit[5] = fruit[6] 
fruit[6] = None 
print("빈칸에 None2 이동 후 리스트 : ",fruit)

del(fruit[6])

print("사과 삭제 후 리스트 : ",fruit)