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

if b in a:
    print(f"단어\'{b}\'의 위치:{a.find(b)}")
else:
    print(-1)

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

#문제27: 문자열 패딩 
a = input()
b = int(input())

while len(a) < b:
    a += '*'


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
eles:
    print(f"a / b = {a/b}")

#문제32: 세금 계산기 
a = int(input())
b = int(input())
s= float(a)*(b/100)
print(f"세금: {s:.1f}원")
print(f"세후 금액: {a-s:.1f}원")

#문제33: 논리 연산 테이블 
a = bool(input())
b = bool(input())
print(f"{a} AND {b} = {a and b}")
print(f"{a} OR {b} = {a or b}")
print(f"NOT {a} = {Not {b}}")
print(f"NOT {b} = {Not {a}}")

#문제34: 할인 계산기 
a = int(input())
b = int(input())
s = float(a)*(b/100)
print(f"할인 금액 = {s:.1f}원")
print(f"최종 가격 = {a-s:.1f}원")

#문제35: 큰 수 판별 
a = int(input())
b = int(input())
c = int(input())
if a >b or a>c:
    print(f"가장 큰 수: {a}")
if b >a or b>c:
    print(f"가장 큰 수:{b}")
else:
    print(f"가장 큰 수:{c}")

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
a = list(input())
s = a[0][0] +a[1][0] ?????

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
ch = input()
v = ["a","i","o","e","u"]
c = ???
for i in v:
    if ch in v:
        v.count +=1
    elif ch.isalpha():

#문제44: 근삿값 계산 
a = float(input())
print(f"가장 가까운 정수: {round(a)}")

#문제45: 날짜 유효성 검사 
y,m,d= input().split('-')
if m == 2 and d ==28 or m ==2 and 29:
    print()


        
    














