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

### 파이썬의데이터형
- 파이썬 데이터 형식
    1. 기본 데이터 형식
    - 리터럴
    - 불
    - 숫자형
        - 정수 
        - 실수
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

### 리스트

- 가변형 데이터 형식
- 리스트의 개념

```
하나씩 사용하던 박스(변수)를 한 줄로 붙여 놓은 것이다. 다른 프로그래밍 언어에서 배열(Array)이와 비슷한 개념(리스트 = 배열)
```

- 리스트 생성과 사용법
```
리스트이름 = [값1, 값2, 값3, ...]

ex) aa = [10, 20, 30, 40]

리스트는 첨자를 사용하여 aa[0] 형식으로 접근

print(aa[0]) = 10
aa[1] = 20
```

- 빈 리스트 생성과 항목 추가
```python
aa = [] # 빈 리스트 생성
aa.append(0)  # 변수 0 추가
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)
```

- 변수 항목이 여러개 일 때, (for문을 활용하면 간단)
```python
aa = []
for i in range(0, 100):
    aa.append(0)
len(aa) # 변수의 길이 100 (0~99)
```