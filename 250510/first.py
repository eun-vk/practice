리스트 메소드_append 
li = [ ] 값이 없는 상태  
b = [1,2,3]
c = b 
c. append(123)
print(b)
[1,2,3,123]
c와 b는 동기화 상태이다. 

# 복제 
c = b.copy()
c.qppend(2)
print(b)
[1,2,3]
print(c)
[1,2,3,2] 

#count 
a = [1,2,3,"okay", 1,1,1]
print(a.count(1)) # 4
b = [1,2,3,[1,2,3,4]]
print(b.count(1)
1 은 숫자 
[1,2,3,4] 안에.  있는 1의 타입은 리스트이다

b = [1,2,3,[1,2,3,1]]
s = b.count(3)
3이 나오게 하려면?
print(b.count(1) +b[3].count(1))

#extend 
a = [1,2,3,4] 
b = [5,6,7,8]
#extend(b)
- 리스트 안에 들어갈 항목들이 순회가 가능하다. 
- 문자열은 순회가 가능하다. 
"good" -> 순회 가능 

b.extend(a)
print(b)
순회가능한 반복가능한 데이터를 넣을 수 있는 기능이다. 

#find 리스트에는 없음. 

#index
b = a.index("aaa") a 리스트에서 aaa의 위치를 찾아라. 

#insert: 삽입 
기존에 있던 것에 넣는 것. 
creat는 새로 만드는 것. 
a = [1,2,3,4,5] 
말뚝박기 
끝에 삽입하려면 append 가능 
끝이 아닌 근 전에 삽입을 하려면 insert 

insert(인덱스, 값)
a. insert(0,0)
print(a) 
[0,1,2,3,4,5] 
- 하나씩 밀린다. 
append는 밀리지 않는다. 

pop
후입선출 
a. pop()'
print(a)
[0,1,2,3,4,5] 
리스트 값이 비어있으면 에러가 뜬다. 인덱스 에러 

#미연에 방지하려면?
if len(a) >=1:
          a.pop()
else:
         print("리스트가 비어있습니다.")
len 은 리스트 안에 있는 데이터 수

#remove(값)
c = [1,2,3,1,1]
c.remove(1)
print(c) #[2,3,1,1]
c.remove(1)
print(c) #[2,3,1]
c.remove(50) #Value Error : list.remove(x) : x not in list



#문제 
'''
당신은 작은 도서관의 책 관리 시스템을 개발하고 있습니다. 다음 단계에 
### 1단계: 초기 도서 목록 생성하기
- 'books'리스트에 다음 5권의 책을 추가하세요.: "파이썬 기초","데이터 
'''

#문제1
books = ["파이썬 기초", 
         "데이터 과학 입문",
         "알고리즘의 이해", 
         "머신러닝 실전",
         "파이썬 기초" ]

#문제2
python_count = books.count("파이썬 기초")
print(f"파이썬 기초책은 {python_count}권 있습니다.")

books.append("웹개발의 시작")
print(f"책 추가 후 : {book}")
books.insert(2, "데이터베이스 설계")
print(f"책 삽입 후: {books}")

new_books = ["인공지능 개론","클라우드 컴퓨팅"]

books.extend(new_books)
print(f"여러책 추가 후: {vook}")

#문제3
book.remove("파이썬 기초")
print(f"파이썬 기초 제거 후: {books}")

last_book = books.pop()
print(f"빼낸 마지막 책: {last_book}")
print(f"책 빼낸 후: {books}")

books.sort()
print(f"정렬 후: {books}")
books.reverse()
print(f"역순 정렬 후: {books}")

#문제4
top_books = books[0:3] #book[:3]
print(f"처음 3권: {top_books}")

reversed_selection = books[1:5][::-1]
# reversed_selection = list(reversed(books[1:5]))


#튜플 
'''
1. 불변성, 변경 불가능하다. (개인정보)
2. 수정은 안되나 그 데이터를 활용할 수 있다. 
3. 튜플은 소괄호
4. 리스트보다 기능이 적다. -> 수정이 불가능
5. 인덱싱과 슬라이싱이 가능하다. 
6. 그 데이터를 가져와서 읽고 사용하는 것은 가능
CRUD 생성, 읽기, 업데이트(수정), 삭제  (튜플은 읽기만 가능)
7. 튜플 안에 튜플을 넣을 수 있다. 중첩이 가능하다. 
8. 튜플 안에 리스트가 있을 때 리스트에 접근하면 그 타입은 리스트이다.  튜플 입장에서는 바뀌면 안되지만 리스트 입장까지가면 변경할 수 있다. 
'''
a = (1,2,3, "good")
b = [1,2,3]
print(type(a))

print(a[3]) # 인덱싱 기능 사용 가능
b =a[0:2]
print(b) #튜플에서 슬라이싱 했기 때문에 타입 자체가 튜플이 된다. 

a[3] = "good" #변경은 불가능하다. 

numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
print(numbers.count(5))
print(numbers.index(5)) #index는 5라는 값이 여러가지 있을 때 제일 먼저 찾은 값 하나만 반환한다.

#set 
'''
- 중복을 허용하지 않는다. 
- 집합에서 사용한다. 
- 없는 값을 지울 수 없다. 
- 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8} 
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}") # 기준은 왼쪽이다. 공통분모포함 오른쪽의 항목을 제거함. 
print(f"차집합: {set2 - set1}")

'''

#1 사용자로부터 입력받은 정수 두 개를 더한 결과를 출력하세요
a, b = map(int,input().split())
s = a+b
print(f"a + b = {s}")


#2 문자열을 입력받아 거꾸로 출력하세요 ex)입력받은 문자가  'python so bad' -> 출력 결과는  'dab os nohtyp'
a = input()
print(a[::-1])


#3 숫자를 입력 받아 짝수면 'Even', 홀수면 'Odd'를 출력하세요
a = int(input())
if a %2 ==0:
    print("Even")
else:
    print("Odd")

#4 [1, 2, 3, 4, 5]의 평균을 구하세요
a = [1, 2, 3, 4, 5]
s = sum(a) / len(a)
print(s)


#5 두 리스트를 입력받아 교집합을 출력하세요
a = [1,2,3,4,5]
b = [4,5,6,7,8]
print(f"a와 b의 교집합: {a & b}")

#6 튜플 (1, [2, 3], 4)에서 리스트 요소 3을 100으로 바꾸세요
t = (1, [2, 3], 4)
t[1][1] = 100
print(t)

# 1번 별 피라미드 출력 
'''사용자에게 정수 N을 입력받아 아래와 같은 별 피라미드를 출력하시오. 
(예: N=3)
'''
n = int(input())
for i in range(1,n+1):
    print('*'*(2*i-1))


# 2번 사용자에게 비밀번호를 입력받아, 다음 조건을 모두 만족하면 "유효한 비밀번호"를 출력하시오. 
'''
- 8자 이상
- "!"또는 "#"기호가 포함되어 있음. 
'''
pw = input()
if len(pw) >=8 and ("!" in pw or "#" in pw):
    print("사용 가능한 비밀번호입니다.")
else:
    print("비밀번호 조건을 만족하지 않습니다.")

# 3번 ID와 비밀번호를 입력받고, 다음과 같은 조건이면 로그인 성공이라고 출력하시오. 
'''
ID가 "admin"또는 "user"
비밀번호는 "1,2,3,4"
'''
id,pw = input().split('/')

if id == "admin" or "user":
    if pw == "1234":
        print("로그인 성공")
else:
    print("로그인 실패")

# 4번 딕셔너리 값을 기준으로 내림차순으로 정렬한 리스트를 출력하세요
age = {'person1': 85, 'person2': 95, 'person3': 90}

a = {"a": 3, "b": 1, "c": 2}
b = sorted(a.items(), key=lambda x: x[1], reverse=True)
print(b)



# 5번 구구단 2단부터 9단까지 for문으로 작성해서 출력하세요.

for a in range(2,10):
    for i in range(1,10):
        print(f"{a}*{i}={a*i}")
print()


# [연습문제]
#문제1: 두 수를 더하는 함수를 만드세요. 
def solution(a, b):
    return a+b
solution(5,3) #결과:8

# 문제2: 두 수를 곱하는 함수를 만드세요.
def solution(a, b):
    return a*b

solution(4, 7)  # 결과: 28

# 문제3: 리스트의 모든 숫자를 더하는 함수를 만드세요.
def solution(numbers):
    total = 0
    for i in numbers:
        total += i 
    return total 

solution([1, 2, 3, 4, 5])  # 결과: 15

# 문제4: 리스트의 평균값을 계산하는 함수를 만드세요.
def solution(numbers):
    total = 0
    for i in numbers:
        total +=i
    return total /len(numbers)

solution([10, 20, 30, 40])  # 결과: 25.0

# 문제5: 문자열의 길이를 반환하는 함수를 만드세요.
def solution(text):
    return len(text)
      

solution("파이썬")  # 결과: 3

# 문제6: 리스트에서 가장 큰 수를 찾는 함수를 만드세요.
def solution(numbers):
    return max(numbers)

solution([7, 12, 3, 8, 4])  # 결과: 12

# 문제7: 리스트에서 가장 작은 수를 찾는 함수를 만드세요.
def solution(numbers):
    return min(numbers)

solution([7, 12, 3, 8, 4])  # 결과: 3

# 문제8: 문자열을 n번 반복하는 함수를 만드세요.
def solution(text, n):
    return text *n
        

solution("안녕", 3)  # 결과: "안녕안녕안녕"

# 문제9: 주어진 숫자가 짝수인지 확인하는 함수를 만드세요. (짝수면 True, 홀수면 False 반환)
def solution(number):
    if number%2==0:
        print("True")
    else:
        print("False")

solution(6)  # 결과: True
solution(9)  # 결과: False