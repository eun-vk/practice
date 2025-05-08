#문제38: 조건부 출력 
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
    print(f"학점: F")

