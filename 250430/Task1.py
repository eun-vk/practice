#문제21: 대소문자 변환
a = input()
print(f"대문자: {a.upper()}")
print(f"소문자: {a.lower()}")
print(f"첫 글자만 대문자: {a.title()}")

#문제22: 문자열 슬라이싱 
a = input()
print(f"앞 3글자: {a[0:3]}")
print(f"뒤 3글자: {a[-3:]}")
print(f"거꾸로: {a[::-1]}")

#문제23: 단어 위치 찾기 
a = input("문장을 입력하세요")
b = input("찾을 단어를 입력하세요.")

print(f"단어\'{b}\'의 위치:{a.find(b)}")


#문제24: 문자교체 
a = input()
b = input()
c = input()
print(a.replace(b,c))

#문제25: 문자 출현 횟수 
a = input()
b = input()
print(f"문자\'{b}\'의 출현 횟수: {a.count(b)}")

#문제26: 이메일 유효성 검사 
email = input()
if '@' in email:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")

#문제27: 문자열 패딩(while)
a = input()
b = int(input())

while len(a) < b:
    a += '*'

#문제27: 문자열 패딩 (a.ljust <-> rjust)
a = input()
b = int(input())
c = a.ljust(b,'*')
print(c)


#문제28: 문자열 중앙 문자 
a = input()

if len(a)%2==0:
    print(f"중앙문자: {a[len(a)//2-1]}{a[len(a)//2]}")
else:
    print(f"중앙문자: {a[len(a)//2]}")

#문제29: 특수문자 제거 
a = input()

#문제30: 이스케이프 시퀀스 연습 
print(f"그녀가 말했다: \"안녕하세요\"!")
print(f"이름\t나이\t직업\n홍길동\t\t30\t\t\t개발자")
print(f"안녕!\n반가워요!")

'''#for : 정해진 데이터 내에서 순회하면서 반복
#while : 조건이 참인 동안 계속해서 반복 

#문제 : 1부터 n까지의 합 구하기 
n = int(input("숫자를 입력하세요."))
i = 1 
total = 0
while i<=n:
    total +=1
    i +=1
print(f"1부터 {n}까지의 합은 {total}입니다.")

#문제 : n보다 작은 짝수들의 합 구하기 
n = int(input("숫자를 입력하세요."))
i = 1
total = 0
while i <n:
    if i %2 ==0:
        total +=i
    i += 1 
print(f"1이상 {n} 미만의 짝수의 합은 {total}입니다.")


#예제1: 1부터 5까지 출력하기 
i = 1 
while i <=5:
    print(i)
    i +=1 '''

#문제31: 사칙연산 계산기 
a = int(input())
b = int(input())
c = input()
if c =='+':
    print(f"a + b = {a+b}")
elif c =='-':
    print(f"a - b = {a-b}")
elif c =='*':
    print(f"a * b = {a*b}")
elif: c == '/':
    print(f"a / b = {a/b}")

#문제32: 세금 계산기 
a = int(input())
b = int(input())
s= float(a)*(b/100)
print(f"세금: {s:.1f}원")
print(f"세후 금액: {a-s:.1f}원")

#문제33: 논리 연산 테이블 
a = input()
b = input()
a = a=="True"  
b = b=="True"
'''bool 연산자를 사용하지 않은 이유는 문자열에서 공백에 여부에 따라
공백이면 False, 공백이 아니면True이다. 
그래서 a ==입력받은 문자 True와 같다면 a = True 
그 외의 다른 문자열이면 False를 반환한다.''' 


print(f"{a} AND {b} = {a and b}")
print(f"{a} OR {b} = {a or b}")
print(f"NOT {a} = {Not b}")
print(f"NOT {b} = {Not a}")

#문제34: 할인 계산기 
a = int(input())
b = int(input())
s = float(a)*(b/100)
print(f"할인 금액 = {s:.1f}원")
print(f"최종 가격 = {a-s:.1f}원")

#문제35: 큰 수 판별(if조건문) 
a = int(input())
b = int(input())
c = int(input())
if a >b or a>c:
    print(f"가장 큰 수: {a}")
if b >a or b>c:
    print(f"가장 큰 수:{b}")
else:
    print(f"가장 큰 수:{c}")

#문제35: 큰 수 판별 (max)
a = int(input())
b = int(input())
c = int(input())
print(f"가장 큰 수: {max(a,b,c)}")


#문제36: 윤년 판별 
a = int(input())
if a%4==0 and a%100 != 0 or a%400 ==0:
    print(f"{a}년은 윤년입니다.")
else:
    print(print(f"{a}년은 윤년이 아닙니다."))

#문제37: 문자열 포함 여부 
a = input()
b = input()
if b in a:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있습니다.")
else:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있지 않습니다.")

#문제38: 조건부 출력 
a = int(input())
if  a >=90:
    print(f"학점: A")
elif a >=80:
    print(f"학점: B")
elif a >=70:
    print(f"학점: C")
elif a >=60:
    print(f"학점: D")
else:
    print(f"학점: F")

#문제39: 자릿수 합계
a = input()
b = sum(int(c) for c in a)
print(f"자릿 수 합계 : {b}")

#문제40: 복합 조건
a = int(input())
b = input()
if a >= 19:
    if b == "Y":
        print(f"입장료: 8000원")
    else:
        print(f"입장료: 10000원")
else:
    print(f"입장료: 5000원")
    
#문제41: 비밀번호 강도 검사 


#문제42: 단어 뒤집기 
a = input().split()
a1 = a[0][::-1]
a2 = a[1][::-1]
a3 = a[2][::-1]
print(a1,a2,a3)

#문제43: 문자 카운터 




    


    

#문제44: 근삿값 계산 
a = float(input())
print(f"가장 가까운 정수: {round(a)}")

#문제45: 날짜 유효성 검사 
y,m,d= map(int,input().split('-'))

if m < 1 or m > 12: #월에 대한 유효성 검사: 모두 int로 바꿨기 때문. 
    print("유효하지 않은 날짜입니다.")
    
else: #월에 대한 일수 설정 
    if m == 2:
        if (y%4 ==0 and y%100 != 0) or y%400 ==0:
            max_day = 29
        else:
            max_day = 28
    elif m in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    if 1 <= d <= max_day:
        print("유효한 날짜입니다.")
    else:
        print("유효하지 않은 날짜입니다.")

#문제46 : 파일 확장자 추출 
a = input().split('.')
print(f"확장자: {a[1]}")

#문제47 : 문자열 압축 




#문제48 : 팰린드롬 검사 
a= input()
b = a[::-1]
if a == b:
    print(f"\'{a}\'은 팰린드롬입니다.")
else:
    print(f"\'{a}\'은 팰린드롬이 아닙니다.")

# 문제 49 : 간단한 암호화 
a = input()
for i in a:
    print(chr(ord(i)+3), end="")


# 문제 50 : IP주소 검증 

    



'''for 변수 in 반복가능한 것:
    실행할 코드 '''

for c in "hello": #hello는 반복 가능한 시퀀스형 자료다. 
    print(c) #hello 문자열 안에서 문자를 하나씩 꺼내서 그 값을 c라는 변수에 담아서 반복한다. 

a= ["apple", "banana", "cherry"]
for b in a:
    print(b)

for i in range(5)
print(i) #range는 0~4까지의 수를 5번 반복한다. 

for i in range(1,11):
    if i % 2 ==0:
        print(f"{i}는 짝수입니다.")


i = 1 
while i <=5:
    print(i)
    i +=1

i = 1 
while i <=10:
    print(i)
    i +=1

num = int(input())

while i != 0:
    print(f"{num}을 입력하셨습니다.")
    n








