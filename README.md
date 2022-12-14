# Python

* [자료구조](#자료구조)
* [알고리즘](#알고리즘)
* [파이썬](#파이썬)
* [연산자](#연산자)
* [조건문](#조건문)
* [반복문](#반복문)
* [함수](#함수)
* [파이썬의데이터형](#파이썬의데이터형)
* [리스트](#리스트)
* [딕셔너리](#딕셔너리)
* [세트](#세트)
* [문자열](#문자열)
* [튜플](#튜플)
* [선형리스트](#선형리스트)

## 자료구조

자료구조란 '컴퓨터 프로그래밍 언어에서 효율적인 자료(데이터)의 형태'

`종류`

- 단순 자료구조
    - 정수(int, integer)
    - 실수(float)
    - 문자(char)
    - 문자열(string)<br>
- 선형 자료구조(한 줄 순차적 나열)
    - 리스트
    - 스택
    - 큐<br>
- 비선형 자료구조(하나의 데이터 뒤에 여러 개 노드가 이어지는 형태)
    - 트리
    - 그래프<br>
- 파일 자료구조(파일 내용이 디스크에 저장되는 방식 구분)
    - 순차 파일
    - 색인 파일
    - 직접 파일<br>

## 알고리즘

알고리즘이란 '어떠한 문제를 해결해 가는 논리적인 과정'

- 표현법
    - 일반 언어 표현(자연어 사용)
    - 순서도를 이용한 표현(순서도(Flowchart)는 여러 종류의 상자와 상자를 이어 주는 화살표를 이용하여 명령 순서 표현)
    - 의사코드를 이용한 표현(의사코드(Pseudo Code)는 프로그래밍언어보다는 좀 더 인간의 언어의 가까운 형태)
    - 그림<br>

- 알고리즘은 성능
알고리즘은 여러 개로 해결 할 수 있으면 해결 시간으로 성능을 측정한다.
`a부터 b까지 합계 구하는 공식` = (a + b) * (a 부터 b까지 숫자의 개수)/ 2
<br>

- 시간 복잡도 함수 그래프<br>
![a1s2d3f4g5](https://user-images.githubusercontent.com/85389685/190129750-cf663b72-1b57-4eb1-96d8-e8ce4b7c8509.png)

[자료구조] -> [알고리즘] -> [프로그래밍언어] => [소프트웨어]


## 파이썬

- 기초 문법
1. 변수와 print() 함수<br>
변수는 어떠한 값을 저장하는 메모리 공간
`boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""`<br>
type() 함수 : 변수 타입 보여줌<br>

2. print() 함수
출력 함수
- print("100")은 숫자가 아닌 문자 취급
- print(%d % 100)은 숫자 취급
`숫자 하나 당 %d 하나씩 당담`<br>
- 서식
    - %d, %x, %o = 10진수, 16진수, 8진수
    - %f = 실수(소수점이 붙은 수)
    - %c = 문자 하나로 된 글('a', 'b', '한', '파')
    - %s = 한 글자 이상의 문자열('abcdefg', '가나다')<br>

```
print(100+100) #100 + 100
print("%d" % 100 + 100) #200
```
<br>

3. input() 함수
input() 함수는 키보드로 값을 직접 입력 받아 변수로 저장한다.<br>
var1 = int(input())
var2 = int(input())
print(var1 + var2)은 입력 받은 값을 계산하여 출력한다.<br>


### 연산자

- 연산자
    - =, 대입 연산자
    - +, 더하기
    - -, 뺄셈
    - *, 곱
    - /, 나누기
    - //, 소수점 버린 값(몫)
    - %, 나머지 값
    - **, 제곱
<br>

- 대입 연산자
    - `a += 3, a = a + 3`
    - +=
    - -=
    - *=
    - /=
    - //=
    - %=
    - **=
 <br>   

- 관계 연산자
    - ==, 같다(두 값이 같아야 참)
    - !=, 같지 않다(두 값이 달라야 참)
    -  >, 크다
    - <, 작다
    - >=, 크거나 같다
    - <=, 작거나 같다
    <br>
`a, b = 100, 200`
print(a==b, a != b, a>b, a<b, a>=b, a<=b)
결과는 참(True)과 거짓(False)으로 나눈다.
주로, 조건문(if)나 반복문(while)에서 사용되며 단독으로 사용되는 경우는 적다.

- 문자열과 숫자의 상호 변환
숫자로 구성된 문자열은 int(), float()함수로 정수나 실수 변환이 잘 되며 숫자를 문자열로 변환할 때에는 str() 함수를 사용한다.

### 조건문
- 기본 if문
```python
a = 99
if a< 100:
    print("100보다 작군요.")
```
<br>
참일 때 print문 출력, 거짓일 때는 아무것도 실행하지 않는다.

<br>

- if~else문
```python
a = 200
if a < 100:
    print("100보다 작군요")
else :
    print("100보다 크군요")
```

<br>
조건식이 참일 때, 실행할 문장 1 -> 조건식이 거짓일 때, 실행할 문장 2 실행

<br>

### 반복문

- for 문
    - 동일하게 반복하는 문장을 간략하게 표현 가능

```python
for 변수 in range(시작값, 끝값+1, 증가값):
    (이 부분 반복)
```

- while 문
    - 반복 횟수를 결정하는 것이 아닌 조건식이 참일 때 반복하는 방식(무한루프)

```python
while True:
    print("g", end = " ")
```

- break 문
    - while 반복문을 논리적으로 빠져나가는 방법(for문에도사용)
```python
for i in range(1, 100):
    print("for 문을 %d번 실행했습니다." %i)
    break
    #1번 실행하고 break문을 만나 종료
```
- continue 문
    - continue문을 만나면 블록의 남은 부분을 무조건 건너뛰고 반복문의 처음으로 돌아간다.(즉, 반복문 처음부터 다시 수행)

### 함수

- 함수의 개념
    - 함수(function)은 `무엇을 넣으면 어떤 것을 돌려주는 요술 상자`
    - 파이썬이 제공하는 함수 형식 `함수이름()`
    - 사용자가 직접 함수를 만들어 사용가능
    - 지역 변수는 한정된 지역(local)에서 사용하는 변수, 전역 변수는 프로그램 전체(global)에 사용하는 변수
    - global 예약어는 예를 들어 a를 전역 변수로 지정하면 더이상 지역 변수 a는 존재하지 않는다.
    - 반환 값이 여러 개인 함수는 문법 상 반환 값이 2개 이상일 수 없음에도 코드를 작성하다보면 종종 값을 2개 반환해야 할 때가 있는데 이때는 리스트에 반환할 값을 넣은 후 리스트를 반환하면 된다.
    <br>

## 파이썬의데이터형
<br>

- 파이썬 데이터 형식
    1. 기본 데이터 형식
    - 리터럴(Literal)
    - 불(bool)
    - 숫자형
        - 정수 (int)
        - 실수 (float)
    2. 연속 데이터 형식
    - 가변형
        - 배열(리스트)(list)
        - 딕셔너리(dict)
        - 세트(set)
    - 불변형
        - 문자열(str)
        - 튜플(tuple)

<br>

- 리터널(Literal)은 숫자, 문자열 등 상수 값을 직접 표기한 데이터를 의마한다. (ex. 100, 1.23, "PYTHON" 등) 

<br>

- 불(BOOL)은 참이나 거짓을 저장할 수 있고 if문, while문의 조건식 결과로 주로 사용
```python
boolVar = 100 > 200
boolVar
type(boolVar)
'''------------------
False
<class 'bool'>'''
```
<br>

- 숫자형에는 정수(int)와 실수(float)가 있다. 다른 프로그래밍 언어는 정수를 short, int, long으로 구분하여 최대 크기도 각각 다르지만 파이썬은 int하나고 크기에도 제한이 없다.
```python
intVar = 100** 100
intVar
type(intVar)
```
<br>

### 리스트
<br>

- 가변형 데이터 형식
- 리스트의 개념

```
하나씩 사용하던 박스(변수)를 한 줄로 붙여 놓은 것이다. 다른 프로그래밍 언어에서 배열(Array)이와 비슷한 개념(리스트 = 배열)
```
<br>


- 리스트 생성과 사용법
```
리스트이름 = [값1, 값2, 값3, ...]

ex) aa = [10, 20, 30, 40]

리스트는 첨자를 사용하여 aa[0] 형식으로 접근

print(aa[0]) = 10
aa[1] = 20
```
<br>


- 빈 리스트 생성과 항목 추가
```python
aa = [] # 빈 리스트 생성
aa.append(0)  # 변수 0 추가
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)
```
<br>

- 변수 항목이 여러개 일 때, (for문을 활용하면 간단)
```python
aa = []
for i in range(0, 100):
    aa.append(0)
len(aa) # 변수의 길이 100 (0~99)
```
<br>


- 리스트 값에 접근하는 방법
    - 생성된 리스트는 첨자로 접근 가능. 여러 번 리스트이름[첨자] 형식으로 접근했다.
    - 음수 접근은 -1부터 시작
```python
aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1], aa[-2])) #출력 40, 30
```
<br>

- 콜론(:)을 사용하여 리스트 범위 지정 : 리스트이름[시작값:끝값 + 1]
- ex) aa[0:3]은 [0]부터 [2]까지
```python
aa = [10, 20, 30, 40]
aa[0:3] #10, 20, 30
aa[2:4] #30, 40
```
<br>


- 콜란의 앞이나 뒤 숫자 생략가능
```python
aa = [10, 20, 30, 40]
aa[2:] #30, 40
aa[:2] #10, 20
```
<br>


- 리스트 조작 함수
    - append() : 리스트 맨 뒤에 항목 추가 #리스트이름.append(값)
    - pop() : 리스트 맨 뒤에 항목을 빼냄(리스트에서 해당 항목 삭제) #리스트이름.pop()
    - sort() : 리스트의 항목 정력 # 리스트이름.sort()
    - reverse() : 리스트 항목의 순서를 역순으로 만듬 # 리스트이름.reverse() 
    - index() : 지정한 값을 찾아 위치를 반환한다 # 리스트이름.index(찾을값)
    - insert() : 지정한 위치에 값을 삽입 # 리스트이름.insert(위치, 값)
    - remove() : 리스트에서 지정한 값을 제거(지정한 값이 여러개이면 첫 번째 값만 지움) # 리스트이름.remove(지울값)
    - extend() : 리스트 뒤에 리스트를 추가(리스트의 더하기(+) 연산과 기능이 동일) # 리스트이름.extend(추가할리스트)
    - count() : 리스트에서 해당 값의 개수를 센다 # 리스트이름.count(찾을값)
    - clear() : 리스트 내용을 모두 지운다 # 리스트이름.clear()
    - del() : 리스트에서 해당 위치의 항목을 삭제 # del(리스트이름[위치])
    - len() : 리스트에 포함된 전체 항목의 개수를 센다 # len(리스트이름)
    - copy() : 리스트 내용을 새로운 리스트에 복사한다 # 새리스트 = 리스트이름.copy()
    - sorted() : 리스트의 항목을 정렬해서 새로운 리스트에 대입 # 새리스트 = sorted(리스트)
<br>

- 2차원 리스트
2차원 리스트는 1차원 리스트를 여러 개 연결한 것으로 첨자를 2개 사용한다.

- 1차원 리스트 개념 aa = [10, 20, 30]
- 2차원 리스트 개념 aa = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]]
                         3행 4열
                    
- 컴프리헨션
`컨프리헨션(함축)`은 값이 순차적인 리스트를 한 줄로 만드는 간단한 방법이다.

<br>

```python
numList = []
for num in range(1, 6):
    numList.append(num) #1, 2, 3, 4, 5
numList #print(numList)
#출력 [1, 2, 3, 4, 5]
```
이 코드를 컨프리헨션으로 바꾸면
<br>

```python
numList = [num for num in range(1, 6)]
numList
```
<br>

```리스트 = [수식 for 항목 in range() if 조건식]```

<br>

- 제곱 구성 리스트
```python
numList = [num * num for num in range(1, 6)]
print(numList)
```

<br>

- if문 추가 3의 배수로만 리스트 구성
```python
numList = [num for num in range(1, 21) if num % 3 == 0]
print(numList)
```

<br>

- 2차원 컴프리헨션
형식 ```리스트 = [[수식 for 항목 in range()] for 항목 in range()]```
```python
list2 = [[0 for _ in range(4)] for _ in range(3)]
print(list2)
```

<br>

### 딕셔너리
<br>

> * 딕셔너리는 가변형데이터 형식이고, 영어 사전이나 국어 사전을 생각하면 된다. 딕셔너리는 쌍 2개가 하나로 묶인 자료구조이며 `apple:사과` 이렇게 의미 있는 두 값을 연결하여 구성한다.
> * 딕셔너리는 중괄호 {}로 묶어 구성하며 키(Key)와 값(Value)의 쌍으로 구성되어 있다.

`딕셔너리변수 = {키1:값1, 키2:값2, 키3:값3, ...}`

<br>

- 딕셔너리 생성
```python
dic1 = {1 : 'a', 2 : 'b', 3 : 'c'}
dic1
```

<br>

반대로 생성 가능
```python
dic1 = {'a' : 1, 'b' : 2, 'c' : 3}
dic1
```


> * 키와 값은 사용자가 지정하는 것으므로 어떤 값을 반드시 사용해야한다는 규정은 없다. 주의할 점은 딕셔너리에는 순서가 없어 생성한 순서대로 딕셔너리가 구성되어 있다는 보장을 할 수 없다.

<br>

- 딕셔너리 생성
```python
stu1 = {'학번' : 1000, '이름' : '홍길동' , '학과':'컴퓨터학과'}
print(stu1)
#{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
```
<br>

- 딕셔너리 추가
```python
stu1['연락처'] = '010-0000-1111'
print(stu1)
#{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과', '연락처': '010-0000-1111'}
```

<br>

- 중복 키 값 입력 시 새로운 쌍이 추가되는 것이 아닌 기존의 값이 변경된다. 딕셔너리 특성상 키는 유일해야하기 때문이다.

<br>

- 딕셔너리 삭제
```python
del(stu1['학과'])
print(stu1)
#{'학번': 1000, '이름': '홍길동', '연락처': '010-0000-1111'}  
```

- 딕셔너리 중복 키 처리(마지막에 있는 키가 적용)
```python
stu1 = {'학번' : 1000, '이름' : '홍길동' , '학과':'컴퓨터학과', '학번' : 2000}
print(stu1)
#{'학번': 2000, '이름': '홍길동', '학과': '컴퓨터학과'}
```

<br>

- 딕셔너리 사용
```python
#키로 값에 접근하는 코드
print(stu1['학번'])
print(stu1['이름'])
print(stu1['학과'])
```
<br>

- 딕셔너리 제공 함수(딕셔너리.get(키))
```python
stu1.get('이름')
```
- 딕셔너리이름[키]는 없는 키를 호출하면 오류 발생
- 딕셔너리.get(키)는 없는 키 호출 시 아무것도 반환하지 않는다.

<br>

- 딕셔너리 모든 키 반환
```python
print(stu1.keys())
#dict_keys(['학번', '이름', '학과'])

#dict_keys가 보기 싫으면
list(stu1.keys())
```

<br>

- 딕셔너리이름.values()함수는 딕셔너리의 모든 값을 리스트로 만들어 반환
```python
#딕셔너리 모든 값 반환
stu1.values()
print(list(stu1.values()))
```

- 딕셔너리 안에 해당 키 유무 확인
(in)
```python
'이름' in stu1
'주소' in stu1
#True
#False
```
<br>

### 세트
<br>

> * 세트는 키만 모아 놓은 딕셔너리의 특수한 형태
> * 딕셔너리의 키는 중복되면 안되므로 세트에 들어 있는 값은 항상 유일
> * 세트 생성하는 방법은 딕셔너리처럼 중괄호({}) 사용하지만 : 없이 값을 입력한다
> * 가변형 데이터 형식
<br>

```python
mySet1 = {1,2,3,3,3,4}
mySet1
#{1,2,3,4}
```
<br>

- 결과를 보면 중복된 키는 자동으로 하나만 남는다. 세트의 이런 특성을 잘 활용하면 기능을 편리하게 작성할 수 있다. 예를 들어 편의점에 판매되는 물품 목록을 리스트에 순차적으로 저장한다고 할 때 결산할 판매된 물품의 전체 수량이 아닌 종류만 파악하고 싶다면 다음과 같이 리스트를 세트로 변경한다.

```python
saleList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
print(saleList)
#{'삼각김밥', '바나나', '도시락'}
```

<br>

- set 함수는 리스트, 튜플, 딕셔너리 등을 세트로 변경시켜는 역할을 한다. 세트는 딕셔너리와 같이 별도의 순서로 저장되지 않는다.

<br>

```python
mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}
mySet1 & mySet2 #교집합 {4, 5}
mySet1 | mySet2 #합집합 {1,2,3,4,5,6,7}
mySet1 - mySet2 #차집합 {1, 2, 3}
mySet1 ^ mySet2 #대칭 차집합 {1, 2, 3, 6, 7}
```
- 이렇게도 표현
```python
mySet1.intersection(mySet2) #교집합
mySet1.union(mySet2) #합집합
mySet1.difference(mySet2) #차집합
mySet1.symmetric_difference(mySet2) #대칭 차집합
```

### 문자열
<br>

> * 문자열은 문자를 연속해서 저장해 놓은 데이터 형식으로, 파이썬에서는 문자열을 큰따옴표(" ")나 작은따옴표(' ')로 묶어서 표현한다. 문자열은 한번 데이터를 저장해 놓으면 변경할 수 없는 불변형 데이터 형식이다.
<br>

- 문자열 기본
    - 리스트는 [ ]로 묶고, 문자열은 따옴표로 묶는다.
    ```python
    ss = "자료구조 & 알고리즘"
    ss[0]
    ss[1:4]
    ss[4:]
    #'자'
    #'료구조'
    #&알고리즘

    #뛰어쓰기도 문자열의 하나로 봄
    ```

    <br>

    - 더하기(+), 곱하기(*) 기호를 사용하여 문자열 반복 가능
    ```python
    ss = '파이썬' + '최고'
    ss
    ss = '파이썬' * 3
    ss
    #파이썬최고
    #파이썬파이썬파이썬
    ```
    <br>

    - 문자열 길이 파악
    ```python
    ss = '파이썬abcd'
    print(len(ss))
    #7
    ```
    <br>

- 문자열 검색
    - count(), find(), rfind(), index(), rindex() 함수를 사용하면 문자열을 찾을 수 있다.
    ```python
    ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
    ss.count('공부')
    print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
    print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
    print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^'))

    #출력
    #2
    #4 21 21 -1
    #4 21 21
    #True False True
    ```
    <br>

    > * `count('찾을문자열')` 함수는 `찾을 문자열`이 몇 개 들어 있는지 세어주는 함수이다.
    > * `find('찾을문자열')` 함수는 `찾을문자열`이 왼쪽 끝(0번 위치)부터 시작해서 몇 번째에 위치하는지 찾는다.
    > * `rfind('찾을문자열')` 함수는 find()와 반대로 `찾을문자열`을 오른쪽부터 찾는다.
    순서 번호는 왼쪽에서 출발한 번호
    > * `find('공부', 5)`는 왼쪽에서 5번째 글자(`부`) 부터 시작
    > * 찾을라는 문자열이 없으면 -1 반환
    > * `index()`함수도 find()와 동일하지만 없는 문자열을 찾으면 오류가 발생

<br>

(중요)
# - 문자열 분리와 결합

> * split()  함수는 `문자열을 공백이나 다른 문자로 분리`하여 리스트를 반환한다.
> * join() 함수는 문자열을 서로 합친다.
<br>

```python
ss = 'Python을 열심히 공부 중'
ss.split()
ss = '하나:둘:셋'
ss.split(':')
ss = '하나\n둘\n셋'
ss.splitlines()
ss = '%'
ss.join('파이썬')

#출력
'''
['Python을', '열심히', '공부', '중']
['하나', '둘', '셋']
['하나', '둘', '셋']
파%이%썬
'''
```
\n은 행이 넘어가는 특수 문자
splitlines() 함수는 행 단위로 분리시켜 준다.

<br>

- 함수 이름 대입
    - map(함수이름, 리스트이름)함수는 리스트의 문자열 하나하나를 함수 이름에 대입한다.
```python
before = ['2022', '12', '31']
after = list(map(int, before))
after

#출력
[2022, 12, 31]
#문자열로 구성된 리스트를 숫자형으로 변환
```

### 튜플
> 튜플은 리스트와 사용법이 비슷하면서 약간 다르며 리스트는 대괄호([ ])로 생성하지만 튜플은 소괄호 ( )를 사용하여 생성한다.
> 또한 튜플은 값을 수정할 수 없으며, 읽기만 가능한 읽기 전용 자료를 저장할 때 사용한다.
<br>

- 튜플 생성과 삭제
```python
tt1 = (10, 20, 30); 
tt1
tt2 = 10, 20, 30; 
tt2

#출력
(10, 20, 30)
(10, 20, 30)

# 튜플은 소괄호()를 생략해도된다.
```

- ## 주의할 점
```python
tt3 = (10);
tt3
tt4 = 10;
tt4
tt5 = (10,); # <--
tt5
tt6 = 10,; # <--
tt6

#출력
'''
10
10
(10,) <--
(10,) <--
'''
# tt3, tt4는 튜플이 아닌 일반값
# 따라서 항목이 하나인 튜플을 만들 때는 tt5, tt6처럼 ,를 붙쳐야 한다.
```

## 튜플은 읽기 전용이다

```python
tt1.append(40)
tt1[0] = 40
del(tt1[0])

#는 모두 오류가 발생

#하지만

del(tt1)
del(tt2)

#이 경우는 튜플 자체를 삭제가능
```
<br>

- 튜플 사용  
튜플 항목에 접근할 때는 리스트처럼 `튜플이름[위치]`를 사용  
```python
tt1 = (10, 20, 30, 40)
tt1[0]
tt1[0] + tt1[1] + tt1[2]


#출력
'''
10
60
'''
```  
- 튜플 범위 접근  
튜플 범위에 접근하려면 리스트와 마찬가지로 `(시작값:끝값+1)`을 사용한다.  
```python
tt1[1:3]
tt1[1:]
tt1[:3]

#출력
'''
(20, 30)
(20, 30, 40)
(10, 20, 30)
'''
```
- 튜플의 덧셈 및 곱셈 연산
```python
tt2 = ('A', 'B')
tt1 + tt2
tt2 * 3

#출력
'''
(10, 20, 30, 40, 'A', 'B')
('A', 'B', 'A', 'B', 'A', 'B')
'''
```

- ## 튜플과 리스트는 서로 변환 가능  
`list(튜플)`함수는 튜플을 리스트로 변환  
`tuple(리스트)`함수는 리스트를 튜플로 변환  
```python
#튜플 -> 리스트 -> 튜플
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
myTuple

#출력
'(10, 20, 30, 40)'
```
<br>

---

# 선형리스트  


> ## 선형 리스트의 기본  

1. 선형 리스트의 개념  
선형 리스트(Linear List)는 데이터를 일정한 순서로 나열한 자료구조  
<br>
ex) 좋아하는 순위 = '1위:딸기', '2위:바나나', '3위:포도', '4위:사과', '5위:배'  
(실제 메모리는 물리적인 순서가 아닌 개념적 순서로 저장된다.)  
<br>
`리스트 = 배열`

2. 선형 리스트의 원리  
(선형 리스트의 데이터 삭제와 삽입)  
<br>

- 데이터 삽입  
선형 리스트에 데이터를 삽입하는 과정 중 2위와 3위 사이에 새로운 데이터인 복숭아를 넣을라고하는데 빈틈이 없다면 맨 끝에 빈칸을 확보한 후 3위부터 5위 자리를 옮겨 3위자리를 비워준 후 복숭아를 삽입한다.   

- 데이터 삭제  
데이터 삭제 후 생기는 빈칸을 선형 리스트는 그대로 두지 않기 때문에 삭제된 데이터 뒤에 있던 데이터들이 앞으로 한 칸씩 이동시킨 후 맨 마지막 빈칸을 제거한다.  

---
<br>

> ## 선형 리스트의 간단 구현

1. 데이터가 5개인 선형 리스트 생성
```python
fruit = ["바나나", "딸기", "포도", "사과", "감귤"]
print(fruit)

#출력
['바나나', '딸기', '포도', '사과', '감귤']
```
배열은 0번째부터 시작함

2. 데이터 삽입
```python
fruit.append(None) #빈칸 삽입
print(fruit)

#출력
['바나나', '딸기', '포도', '사과', '감귤', None]
```
```python
fruit[5] = "배" #빈칸에 데이터 삽입
print(fruit)

#출력
['바나나', '딸기', '포도', '사과', '감귤', '배']
```

- 데이터 중간에 데이터 삽입하기
```python
#1
fruit.append(None) #빈칸 삽입
print(fruit)

#출력
['바나나', '딸기', '포도', '사과', '감귤', '배', None]
```
```python
#2
fruit[6] = fruit[5] #동일시 하기
fruit[5] = None # 빈칸으로 만들기
print(fruit)

#출력
['바나나', '딸기', '포도', '사과', '감귤', None, '배']
```
```python
fruit[5] = fruit[4] 
fruit[4] = None 
fruit[4] = fruit[3] 
fruit[3] = None 
print(fruit)

#출력
['바나나', '딸기', '포도',  None, '사과', '감귤', '배']
```
```python
fruit[3] = "망고"
print(fruit)

#출력
['바나나', '딸기', '포도',  '망고', '사과', '감귤', '배']
```

3. 데이터 삭제
```python
fruit[4] = None
fruit[4] = fruit[5] 
fruit[5] = None 
fruit[5] = fruit[6] 
fruit[6] = None 

del(fruit[6])

print(fruit)

#출력
['바나나', '딸기', '포도',  '망고', None, '감귤', '배']
['바나나', '딸기', '포도',  '망고', '감귤', None,'배']
['바나나', '딸기', '포도',  '망고', '감귤', '배',None]
['바나나', '딸기', '포도',  '망고', '감귤', '배']
```
---
> ## 선형 리스트의 일반 구현

<br>

1. 배열을 이용한 선형 리스트 생성    
```python
katok = []

katok.append(None)
배열길이 = len(katok)
katok[배열길이 - 1] = '다현'
print(katok)

#출력
['다현']


katok.append(None)
배열길이 = len(katok)
print(배열길이) # 2
katok[배열길이 - 1] = '정연' #katok[1]
print(katok) #['다현', '정연']
```
2. 선형 리스트 생성 함수의 완성  
- 선형 리스트의 끝에 데이터를 추가하는 함수를 작성해서 5명을 차례대로 추가하는 완전한 코드 만들기
```python
katok = [] #빈 배열을 전역변수로 정의

def add_data(friend):

    katok.append(None) #맨 뒤칸에 None추가
    KLen = len(katok) #변수 길이
    katok[KLen - 1] = friend #맨 뒤칸에 변수 추가

add_data('영지')
add_data('서준')
add_data('효주')
add_data('사나')
add_data('유진')

print(katok)
```
3. 데이터 삽입
선형 리스트에 데이터를 삽입하는 방식 구현
- 중간 데이터 삽입
```python
katok.append(None) #선형 리스트에 빈칸 추가

for 현재위치 in range(마지막위치, 지정위치, -1):
    katok[현재위치] = katok[현재위치 - 1]
    katok[현재위치 - 1] = None
    #빈칸을 중간 자리에 이동

katok[지정위치] = friend
#중간에 있는 빈칸을 지정하여 데이터 추가
```

- 맨 끝 데이터 삽입
```python
katok.append[None]

for 현재위치 in range(마지막위치, 지정위치, -1): #작동하지 않음
    katok[현재위치] = katok[현재위치 -1]
    katok[현재위치 - 1] = None

    katok[지정위치] = friend #데이터 추가
```

4. 데이터 삽입 함수의 완성
```python
#Code03-02.py

katok = ["다현", "정연", "쯔위", "사나", "지효"]

def insert_data(position, friend):

    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None) #빈칸 추가
    KLen = len(katok) #배열의 현재 크기

    #(마지막 위치, 지정위치, -1)
    #KLen - 1 '마지막 위치' =전체 길이가 6이면 마지막 인덱스는 5
    for i in range(KLen - 1, position, -1): 
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend #지정한 위치에 친구 추가

insert_data(2, '솔라') #함수 작동
print(katok)
insert_data(6, '문별')
print(katok)


'''
for문 range(값1, 값2, 값3)에서 값1과 값2가 같으면 한번도 수행하지 않는다.
'''
```

5. 데이터 삭제
- 중간 데이터 삭제  
중간에 있는 데이터를 삭제 후 생긴 **빈칸**에 뒤에 있는 데이터들을 땡겨와 채워 준 후 맨 뒤에 생긴 빈칸을 삭제한다.
```python
katok[지정위치] = None

for 현재위치 in range(지정위치 + 1, 마지막위치 + 1):
    katok[현재위치 - 1] = katok[현재위치]
    katok[현재위치] = None

    del(katok[지정위치])
```

- 맨 마지막 데이터 삭제
```python
katok[지정위치] = None

for 현재위치 in range(지정위치 + 1, 마지막위치 + 1):
    katok[현재위치 - 1] = katok[현재위치]
    katok[현재위치] = None

    del(katok[지정위치])

#삭제 위치가 중간이든 마지막이든 동일한 코드 작동
```

- 데이터 삭제 함수의 완성
```python
#Code03-03.py

katok = ["다현", "정연", "쯔위", "사나", "지효"]

def delete_data(position):

    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    KLen = len(katok) #배열의 현재 크기
    katok[position] = None #데이터 삭제

    #position + 1은 삭제한 다음 위치
    for i in range(position + 1, KLen): 
        katok[i - 1] = katok[i]
        katok[i] = None #배열 맨 마지막 위치 삭제

    del(katok[KLen - 1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)
```

6. 기본 선형 리스트의 완성
```python
#Code03-04.py
#선형 리스트 처리 프로그램

def add_data(friend):

    katok.append(None)
    KLen = len(katok)
    katok[KLen - 1] = friend

def insert_data(position, friend):

    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None) #빈칸 추가
    KLen = len(katok) #배열의 현재 크기

    for i in range(KLen - 1, position, -1): 
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend #지정한 위치에 친구 추가

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

## 전역 변수 선언
katok = []
select = -1 #1: 추가,  2: 삽입, 3: 삭제, 4: 종료

# 메인코드
if __name__ = "__main__":

    while(select != 4):

        select = int(input("선택하세요(1: 추가,  2: 삽입, 3: 삭제, 4: 종료)-->"))

        if(select == 1):
            data = input("추가할 데이터 -->")
            add_data(data)
            print(katok)
        elif(select == 2):
            pos = int(input("삽입할 위치 -->"))
            data = input("추가할 데이터 -->")
            insert_data(pos, data)
            print(katok)
        elif(select == 3):
            pos = int(input("삭제할 위치-->"))
            delete_data(pos)
            print(katok)
        elif(select == 4):
            print(katok)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
```
---
> 선형 리스트의 응용
1. 다항식의 선형 리스트 표현  
선형 리스트의 가장 많은 응용 중 하나는 다항식(Polynomial)을 저장하고 활용하는 것이다.  

<br>

다항식 형식  
`P(x) = a + bx + cx^2 + dx^3 + ... + zx^n`

<br>

`P(x) = 7x^3 - 4x^2 + 5`  
`P(x) = 7x^3 - 4x^2 + 0X^1 + 5X^0`  

<br>

선형리스트로 표현 하면 `| 7 | -4 | 0 | 5 |` 로 짜여진 배열 완성

```python
px = [7, -4, 0, 5]
print(px)
```
```python
x = 2
pxVal = 7*x**3 - 4*x**2 + 0*x**1 + 5*x**0
print(pxVal) #45
```
```python
px = px = [7, -4, 0, 5]
polyStr = "P(x) = "
polyStr += " + " + str(px[0]) + "x^" + str(3) #x**3
polyStr += " + " + str(px[1]) + "x^" + str(2)
polyStr += " + " + str(px[2]) + "x^" + str(1)
polyStr += " + " + str(px[3]) + "x^" + str(0)
print(polyStr)

# P(x) = 7x^3 + -4x^2 + 0x^1 + 5x^0
```

2. 다항식의 선형 리스트 표현과 계산 프로그램  
- 계산 함수 : calcPoly()
- 다항식 형태 출력 함수 : printPoly()

```python
#Code03-05.py
#다항식 선형 리스트 표현과 계산 프로그램

# 2~14행 30행의 다항식 계수 배열
def printPoly(p_x):
    term = len(p_x) - 1 #최고차항 숫자 = 배열 길이 - 1
    polyStr = "P(x) = " #polyStr에 다항식 형태의 문자열을 만들고자 P(x) 값을 우선 대입

    for i in range(len(px)): #계수x^차수 형식 반복
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr


def calcPoly(xVal, p_x):
    retValue = 0 #계산할 다항식을 0으로 초기화
    term = len(p_x) - 1 #최고차항 숫자 = 배열 길이 - 1, 크기가 4라면 최고차항은 x^3이 된다.
    
    for i in range(len(px)):
        coef = p_x[i] #계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue
# 배열 개수만큼 다항식 계산, 22행에서 계수를 추출하고 23행에서 "계수 * x값 ** 차수"를 계산한다. 24행에서 항의 차수를 1 감소시킨다.

#전역 변수
px = [7, -4, 0, 5] #7x^3 + -4x^2 + 0x^1 + 5x^0



if __name__ == "__main__":

    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값 -->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)
```
3. 특수 다항식 처리 프로그램
- 지수가 상당히 큰 다항식은 어떻게 처리하는지  

`ex)`  
- P(x) 7x^300 + (-4)x^20 + 5
```python
px = [7, -4, 0, 5] #7x^3 + -4x^2 + 0x^1 + 5x^0
'이 부분을 0000000000000000000000000000.....으로 선언해야한다.'
```

<br>

이를 간단히 처리하기 위해 모든 계수를 저장하지 않고 0 이 아닌 계수와 항의 차수와 저장하는 방식을 사용할 수있다.
```python
tx = [300, 20, 0] #항 차수
px = [7, -4, 5] # 각 항 위치의 계수
```

<br>

```python
#Code03-06.py
#특수 다항식의 선형 리스트 표현과 계산 프로그램

#함수 선언
def printPoly(t_x, p_x):
    polyStr = "P(x) ="

    for i in range(len(p_x)):
        term = t_x[i] # 항 차수
        coef = p_x[i] # 계수

        if(coef > 0) :
            polyStr += " + "
        polyStr += str(coef) + "X^" + str(term) + " "
    
    return polyStr

def calcPoly(xVal, t_x, p_x) :
    retValue = 0

    for i in range(len(px)):
        term = t_x[i] # 항 차수
        coef = p_x[i] # 계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue


tx = [300, 20, 0] 
px = [7, -4, 5]


if __name__ == "__main__" :
    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input("X 값 -->"))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)
```