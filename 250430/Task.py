
#문제1: 인사하기 
a = input("이름을 입력해주세요")
print(f"안녕하세요, {a}님!")

#문제2: 에코 프로그램 
a = input()
print(a*3)

#문제3: 나이계산기 
birth = input("출생연도를 입력하세요.")
age = 2025-birth
print(f"당신의 나이는 {age}세입니다.")

#문제4: 원 넓이 계산 
r = int(input())
s = 3.14*r**2
print(f"반지름이 5인 원의 넓이: {s}")

#문제5: 여행 거리 계산 
km = int(input())
h = int(input())
print(f"총 이동 거리: {km*h}km")

#문제6: 문장 합치기 
a = input()
b = input()
print(a+' '+b)

#문제7: 인치-센티미터 변환
a = int(input())
cm = a * 2.54
print(f"{a}인치는 {cm}센티미터입니다.")

#문제8: 팁 계산기 
a = int(input())
b = int(input())
c= a*(b/100)
print(f"팁 금액: {c}원")
print(f"총 지불 금액: {a+c}원")

#문제9: BMI 계산기 
cm = int(input())
kg = int(input())
m = float(cm/100)
print(f"BMI: {kg/m**2}")

#문제10: 다중 입력
a = input().split()
print(f"첫 번째 숫자:{a[0]}")
print(f"마지막 숫자:{a[-1]}")

#문제11: 변수교환 
a = input()
b = input()
print(f"교환 전: a = {a}, b = {b}")
print(f"교환 후: a = {b}, b = {a}")

#문제12: 문자열 정보 출력 
a = input()
print(f"문자열 길이:{len(a)}")
print(f"첫 글자: {a[0]}")
print(f"마지막 글자: {a[-1]}")

#문제13: 이니셜 만들기 
a , b = input().split()
c= a[0].upper()
d= b[0].upper()
print(f"이니셜: {c}.{d}.")

#문제14: 소수점 자릿수 
a = float(input())
print(f"a:.2f")

#문제15: 나이 구간 판별
age = int(input())
if age >= 65:
    print("노년")
elif age >=35:
    print("중장년")
elif age >=19:
    print("청년")
else:
    print("미성년자")

#문제16: 문자열 분석 
a = input()
b = a.count("")
c= sum(a.count(str(i)) for i in range(10))
d= sum(map(str.isalpha, a)) 
print(f"공백 수: {b}")
print(f"숫자 수: {c}")
print(f"문자 수: {d}")
''' 문자열 a의 각 문자에 대해 그 문자가 알파벳이면 True, 
아니면 False.
map은 str.isalpha가 a에 적용될 수 있도록 해줌. 
True = 1, False =0을 반환 
최종적으로 True의 개수를 더하면 문자의 개수를 구할 수 있다.'''  

#문제17: 참/거짓 변환
a = input()
b = int(input())
if a =="":
    print("False")
else:
    print("True")
if b ==0:
    print("False")
else:
    print("True")



#문제18: 홀짝 판별
a = int(input())
if a%2==0:
    print(f"{a}은(는) 짝수입니다.")
else:
    print(f"{a}은(는) 홀수입니다.")

#문제19: 문자열 분할 
a = list(input().split())
s = ','.join(a)
print(s)

#문제20: 온도 단위 변환기 
a = float(input())
b = input()
b = "C" or "F"
if b == "C":
    print(f"{a}ºC는 {a*9/5+32}ºF입니다.")
else:
    print(f"{a}ºF는 {(a-32)*5/9}ºC입니다.")

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





