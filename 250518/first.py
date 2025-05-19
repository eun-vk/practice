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

# x의 n제곱을 구하는 함수를 만들어주세요. 
# 재귀함수를 이용하여 만들어야 하며, x는 0이 아닙니다. (x, n > 1)

def power(x,n):
    if n ==0:
        return 1 
    else: 
        return x**power(x,n-1)
    


# 이 데이터에서 licat을 출력해주세요. 단, 직접 접근은 안됩니다. data[1]로 접근하는 것은 안됩니다.


# 잘못 입력된 문자 때문에 에러가 생길 수 있으므로 사전에 에러를 방지하기 위해 특수문자를 모두 제거하는 코드 작성하기. 
s = '010-1000?2000'
result = ''
for i in s:
    if i.isdigit():
        result += i
print(result)

