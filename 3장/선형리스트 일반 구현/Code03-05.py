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