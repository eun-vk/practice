# 정수 num1, num2가 매개변수로 주어질 때, 
# num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    return num1//num2

# 정수 num1, num2가 매개변수 주어집니다. 
# num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    return num1*num2

# 정수 num1과 num2가 주어질 때, 
# num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

def solution(num1,num2):
    return num1-num2

# 정수 num1과 num2가 주어질 때, 
# num1에서 num2를 더한 값을 return하도록 soltuion 함수를 완성해주세요.

def solution(num1, num2):
    return num1 + num2

# 정수 num1, num2가 매개변수로 주어질 때,
#  num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    return num1 % num2

# 정수 num1과 num2가 매개변수로 주어집니다. 
# 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    if num1 ==num2:
        return 1
    else:
        return -1

def solution(num1, num2):
    answer = 1 if num1 ==num2 else -1
    return answer

def solution(num1, num2):
    answer = {num1 == num2 : 1, num1 != num2 : -1}.get(True, =1)
    return answer

# 머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 
# 2022년 기준 선생님의 나이 age가 주어질 때, 
# 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요

def solution(age):
    return 2022 -age +1


# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 
# 180도는 평각으로 분류합니다. 각 angle이 매개변수로 주어질 때 예각일 때 1, 
# 직각일 때 2,둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

def solution(angle):
    if angel < 90:
        return 1
    elif angel == 90:
        return 2
    elif angel >90:
        return 3
    elif angel ==180:
        return 4
    
#  정수 num1과 num2가 매개변수로 주어질 때, 
#num1을 num2로 나눈 값에 1,000을 곱한 후 
#정수 부분을 return 하도록 solution 함수를 완성해주세요.

def solution(num1,num2):
    return int(num1 / num2 * 1000)


# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

def solution(nembers):
    return sum(numbers)/len(nembers)

# 정수 n이 주어질 때, 
# n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

def solution(n):
    total = 0

    for i in range(1,n+1):
       if i % 2 == 0:
           total += 1
    return total

def solution(n):
    total = 0

    for i in range(n, n+1,2):
        total +=i
    return total


def solution(n): #메모리 효율이 가장 좋다. 
    total = sum(range(2,n+1,2))
    return total


# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
#  array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.  

def solution(array, n):
    '''메모리 사용이 적고, 속도는 O(n)
       한 번만 세는 경우에 적합한 방법'''
    return array.count(n)

from collections import Counter
def solution(array, n):
    return Counter(array).get(n)

# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 
# 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

def solution(array, height):
    total = 0
    for i in array:
        if i > height:
            total += 1
    return total 

def solution(array, height):
    return sum(1 for i in array if i > height)


# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
# 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 
# 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

def solution(n,k):
    free_drinks = n //10
    pay_drinks = k-free_drinks 

    return (n * 12000) + (pay_drinks * 2000)  '''디버깅, 유지보수에 유리'''

def solution(n,k):
    if n >=10:
        k -= n//10
    return (n * 12000) + (k * 2000)           '''k값을 직접 변경하기 때문에 주의'''

def solution(n,k):
    return (12000 * n) + (2000 * (k - n // 10))   '''가독성이 떨어질 수 있고 디버깅이 어려울 수 있지만 가장 빠르고 메모리 효율이 높다. '''

