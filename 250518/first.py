# 함수를 이용하여 계산기 프로그램을 만들어주세요.

def plus(num1, num2):
    return num1+ num2

def minus(num1, num2):
    return  num1 - num2

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 /num2

print(f'plus : {plus(10,5)}')
print(f'minus: {minus(10,5)}')
print(f'multiply : {multiply(10,5)}')
print(f'divide : {divide(10,5)}')


# 2번의 해답을 이용하여 a와 b를 더한 값과 a와 b를 뺀 값을 곱하는 함수를 만들어주세요. 
# 아래와 같은 값이 있다면 (2 + 3) * (2 - 3) = -5가 출력이 되어야 합니다.
a = 2
b = 3

def multiple (x = 0, y = 0):
    return x*y 
def plus(x = 0, y = 0):
    return x + y

def minus(x = 0, y = 0):
    return x - y

multiple(plus(a,b), minus(a,b))
