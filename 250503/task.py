'''#문제38: 조건부 출력 
a = int(input("학점을 입력해주세요."))
if  a >=90:
    print(f"학점: A")
elif a >=80:
    print(f"학점: B")
elif a >=70:
    print(f"학점: C")
elif a >=60:
    print(f"학점: D")
else:
    print(f"학점: F")'''


a = [1,2,3,4]
b = [5,6,7,8]
c = "즐거움"

b.extend(a) # b리스트에 a리스트 값 추가
print(b) # 결과: [5,6,7,8,1,2,3,4]

b.extend(c)
print(b) # 결과: [5,6,7,8,1,2,3,4,"즐","거","움"]