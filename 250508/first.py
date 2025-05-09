#문제20: 온도 단위 변환기 
temp = input()
temp = float(temp)
unit = input() #C 또는 F

if unit == "C":
    convert = temp *9/5 +32
    print(f"t{temp}.C는 {convert}.F입니다.")
elif unit == "F": 
    convert=(temp-32)*5/9
    print(f"{temp}.F는 {conver}.C입니다.")
else:
    print("잘못입력하였습니다.")

#문제1
a = int(input())
b = a - 543
print(b)


#문제2
a, b, c = map(int,input().split())
s = a+ b+ c 
print(s)

print("\\    /\\")
print(" )  ( ')")
print("(  /  ) ")
print(" \\(__)| ")

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")'''

#문제3
'''food = input()
if food.find("짜장") != -1:
    if "쟁반" in food:
        print("쟁반짜장입니다.")
else:
    print("짬뽕입니다.")
    
#문제4
a, b = map(int,input().split())   
if a >b:
    print('>')
elif a <b:
    print('<')
elif a ==b:
    print('==')

#문제5
a = int(input())
if a >=90:
    print("A")
elif a >=80:
    print("B")
elif a >=70:
    print("C")
elif a >=60:
    print("D")
else:
    print("F")

# 1. good이라는 문자열을 인덱싱 기법으로 추출 
c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]

print(c[4][3][1])

# 2. 슬라이싱 기법을 통해 [123,"good"] 을 추출
print(c[4][3][0:2]) #실질적으로 0~1까지 
#stack ->  last in first 마지막으로 들어간 내용이 먼저 나옴. 후입선출
#queue -> 먼저 들어간 사람이 먼저 나온다. 선입선출

a = [1, 2,3, "good"]
a[3] = "aaaa" -> 대체해 버림 
print(a)
a[3][1] = "g" #우리가 의도한 것은 agaa 하지만 이렇게 할 수 없다. 스트링의 문자열 값은 바꿀 수 없다.
#이걸 하려면 그냥 새로운 문자열을 만들어야 한다. 문자열의 특정 문자는 바꿀 수 없다.  
# 리스트 안에 있는 값을 바꿀 수 있다. -> 가변적이다. 중복을 허용한다. 중첩 허용

#리스트의 기능 (append) 데이터 추가 
li = [] #현재 값이 없는 상태 
li.append(1) 
li.append(2) #빈 리스트에 append를 해서 넣어주면 순서는 먼저 입력한 순서대로 입력됨.)
li.append([1,2,3]) #[1,2,[1,2,3]] 이렇게 추출됨. 
li[2].append("good")
print(li)

#데이터 삭제 
li.clear()
print(li) #[] 리스트 안에 있는 데이터 날라감. 리스트 자체는 남아있음. []이런 형식으로. 

#리스트 복제 
b = [1,2,3]
c = b 
c.append(123) #원래 의도는 c에만 123을 추가 하고 싶음. b와 c동기화 연동되었다. 
print(b) # 결과 [1,2,3,123] 이렇게 출력됨. 그래서 이렇게는 복제가 안 됨. 

c = b.copy()
c.append(2)
print(b) #[1,2,3]
print(c) #[1,2,3,2]


빈리스트를 만든다.
append를 사용하여 이중 리스트를 만든다.
출력한다.
리스트의 데이터를 다 지운다.
출력한다.
copy를 활용한다.
카피를 활용한 리스트에 append를 사용하여 출력한다.

a = [ ]
#a.append(1,2,["사과", "바나나",[24,0],25],5,"과일") #리스트는 오직 하나의 값만 받을 수 있는 함수.하나의 값을 리스트 끝에 추가하는 구조 

a.append(33)
a.append(["사과","바나나"])
print(a)

a.clear(a)
print(a)
b = a.copy()
b.append(3)
print(b)

a = [1,2,3,"okey", 1,1,1]
print(a.count(1))

b[1,2,3,[1,2,3,1]]
print(b.count(1)) #출력 : 1 why? 1은 숫자, [1,2,3,1]안에 있는 1은 타입이 숫자 1이 아니라 리스트이다. 매칭이 안되기 때문에 

b[1,2,3,[1,2,3,1]]
print(b[2])
print(b[3][2])
print(b.count(1) +b[3].count(1)) #Itertools 반복가능한, 순회 가능한.

#확장 extend 반복되는 데이터를 넣을 수 있는 기능 
a.extend(b)
print(a)
c = "good"
b.extend(c)
print(b) #[5,6,7,8,'g','o','o','d']

a = ["good","okey"]
b = a.index("aaaa")
print(b) #ValueError: 'aaaa'is not in list
c = a.index("okey")
print(c)

list 
중복데이터 있을 수 있고 중복 리스트 만들 수 있다. 
stack형이다. 
왼쪽에서 오른쪽으로 자료가 쌓인다. 
list에서 지원하는 기능을 잘 알아야 한다. find는 지원 안 됨. 

#insert 그 구조를 뛰어 들어가서 바꾸는 것. 오른쪽에 있는 데이터는 밀림. 

디스코드에 예쁜 색 넣기 
```python```


'''종합 실습: 도서관 관리 시스템 구현하기
아래 문제를 통해 파이썬 리스트의 다양한 기능을 활용해봅시다. 도서관 책 관리 시스템을 만드는 과정에서 리스트의 여러 메서드를 실습해볼 것입니다.

문제
당신은 작은 도서관의 책 관리 시스템을 개발하고 있습니다. 다음 단계에 따라 리스트를 활용한 책 관리 시스템을 구현해보세요.

1단계: 초기 도서 목록 생성하기
books 리스트에 다음 5권의 책을 추가하세요: "파이썬 기초", "데이터 과학 입문", "알고리즘의 이해", "머신러닝 실전", "파이썬 기초"
books 리스트를 출력하세요.'''

books =["파이썬 기초", "데이터 과학 입문", "알고리즘의 이해", "머신러닝 실전","파이썬 기초"]
print(books)



'''2단계: 책 목록 관리하기
목록에서 "파이썬 기초"가 몇 권 있는지 확인하세요.
"웹 개발의 시작"이라는 책을 목록 끝에 추가하세요.
"데이터베이스 설계"라는 책을 3번째 위치에 삽입하세요.
새로운 책 리스트 new_books를 만들고 ["인공지능 개론", "클라우드 컴퓨팅"]을 포함시킨 후, books 리스트에 추가하세요.
수정된 books 리스트를 출력하세요.'''

python_count = books.count("파이썬 기초")
print(f"파이썬 기초 책은 {python_count}")

books.append("웹 개발의 시작")
print(f"책 추가 후: {books}")
books.insert(2,"데이터베이스 설계")
print(f"책 삽입 후: {books}")

new_books = ["인공지능 개론",'클라우드 컴퓨팅']
books.extend(new_books) #books가 기준, 확장함. 
print(f"여러책 추가 후: {books}")


'''3단계: 책 제거 및 관리하기
목록에서 첫 번째로 등장하는 "파이썬 기초"를 제거하세요.
리스트의 마지막 책을 빼내어 변수 last_book에 저장하고, 이 책을 출력하세요.
책 목록을 알파벳 순으로 정렬하세요.
정렬된 목록을 역순으로 뒤집으세요.
수정된 books 리스트를 출력하세요.'''
books.remove("파이썬 기초")
print(f"파이썬 기초 제거 후: {books}")

last_book = books.pop()
print(f"빼낸 마지막 책:{last_book}")
print(f"책 빼낸 후:{books}")

books.sort()
print(f"정렬 후:{books}")

book.reverse()
print(f"역순 정렬 후: {books}")



'''4단계: 도서 목록 분석하기
슬라이싱을 사용하여 books 리스트의 처음 3권을 top_books라는 새 리스트에 저장하세요.
books 리스트에서 2번째부터 5번째까지의 책들을 역순으로 reversed_selection이라는 새 리스트에 저장하세요.
top_books와 reversed_selection을 출력하세요.
books 리스트를 완전히 비우고 출력하세요.'''

top_books=books[0:3] #books[:3]
print(f"처음 3권: {top_books}")

reversed_selection = book[1:5][::-1]
#reversed_selection = list(reversed(books[1:5])) reversed의 반환값은 none


reversed_selection.reversed(books)
print(top_books)
print(reversed_selection)
books.clear()
print(books)

'''튜블의 제일 큰 특징은 수정할 수 없다. 불변하다. '''