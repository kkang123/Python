
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

#2~13행 다항식 형식을 출력, 매개변수 t_x는 29행의 항의 차수 배열이고, p_x는 30행 다항식 계수 배열

#6~11행 polyStr에 "계수x^차수" 형식을 반복해서 추가, 6행에서 항 차수를 추출하고, 7행에서 계수를 추출, 11행에서 "+7x^300" 같은 형식을 만들어서 polyStr에 추가

#16~25행 사용자가 입력한 값으로 다항식을 계산, 매개변수 xVal은 사용자가 입력한 x값이다. t_x는 29행의 항의 차수 배열이고, p_x는 30행 다항식 계수 배열

#19~23행 배열개수만큼 다항식을 계산하고 20행에서 항 차수를 21행에서 계수를 추출한다 그리고 22행에서 "계수*x값**차수"를 계산한다. x 값이 1이라면 처음에는 7*1**300을 계산해서 7을 누적시킨다.

#29~30행 다항식 차수 배열과 계수 배열이다. 어떤 배열 값을 넣어도 다항식이 처리됨

#34~42행은 함수를 테스트하고자 각  함수를 호출하고 결과를 출력하며 39행에서 x 값을 직접 입력 받는다.