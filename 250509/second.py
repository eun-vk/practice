#반복문 
'''
for문은 출력하면 세로 줄로 입력된다. 
왼쪽부터 오른쪽 순서로 읽는다. 
'''
'''s = 'hello'

for i in s:  #for: 반복 , s = 변수 , i :담는 변수
    print(i)

#range(숫자) 0부터 숫자 -1 까지의 범위를 만든다. 
for i in range(5000): # 0 부터 4999까지의 어떤 순회가능한 데이터를 만든다. 
    print(i)

#range(10,51) #10부터 50까지의 범위를 만든다. 
for i in range(10, 51):
    print(i)

# range(1, 11, 2) 1부터 10까지 2계단씩 점프 
for i in range(1,11,2):
    print(i)

#range(5000) == range(0,5000,1)

#내림차순
for i in range(10,2,-1):
    print(i)'''

'''
1부터 100까지 출력
2부터 50까지 짝수만 출력 
10부터 -1까지 출력 
'''

for i in range(1,101):
    print(i)

for i in range(2,51,2):
    print(i)

for i in range(10,-2,-1):
    print(i)

for i in range(1,100): #1부터 99까지 반복한다. 
    if i %3 == 0: #3의 배수이면?
        print(i) #3의 배수만 출력 

# 2~9 구구단 만들기 
for i in range(2, 10): #앞의 2는 고정 
    
    for j in range(1, 10): #9바퀴 돌고 위로 올라간다. 
        print(f"{i}*{j} = {i*j}")
        if i*j == 9 : #9라면 9를 출력 
            print(9)
            
`
#11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num %2 ==0:
       ever_numbers.append(num)
       
print(even_numbers) 


#12
a = int(input())
if a>=100:
       print("수증기")
elif a >=0:
       print("물")
else:
       print("얼음")


#13
average = sum(scores.values()) / 4 
print(f"평균 점수: {average}점")

#14
text = "Python Programming"
r = text.replace(" ","").lower()
print(r)

#15
n = int(input())
t = 0

for i in range(1, n + 1):
    if i % 3 != 0:  
        t += i
print(t)   
`