# 윤년 
year = int(input())
if (year%4 ==0 and year%100!=0) or year%400==0:
    print(1)
else:
    print(0)

#4분면 번호 
num1 = int(input())
num2 = int(input())

if num1 >0 and num2 >0:
    print(1) 
elif num1 <0 and num2 >0:
    print(2) 
elif num1 <0 and num2 <0:
    print(3) 
else:
    print(4)

#오븐 시간
h, m = map(int, input().split())
start = int(input())

m += start 

if m >= 60:
    h+=m//60
    m = m%60

if h >=24:
    h = h % 24

print(h, m)
            

#알람시계
h,m = map(int,input().split())
m -=45

if m <0: 
    m+=60
    h+=-1
    if h <0:
        h =23

print(h,m)

#주사위 문제 
a, b, c = map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a ==b:
    print(1000+a*100)
elif b ==c:
    print(1000+b*100)
elif a ==c:
    print(1000+a*100)
else:
    print(max(a,b,c)*100)


# 구구단 
n = int(input())
for i in range(1,10): #range는 정수 범위를 반복 가능한 객체로 만드는 함수
    print(f"{n} * {i} = {n*i}")
print()

#구구단2
t = int(input())


for i in range(t):
    a, b = map(int,input().split())
    print(a+b)

#합 반복 
n = int(input())
sum = 0
for i in range(1,n+1):
    sum =sum+i # i는 각 반복에서 변화하는 값을 말함. n은 횟수를 정함(고정값)
print(sum)

#영수증 
