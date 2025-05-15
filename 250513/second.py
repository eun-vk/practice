
# 로그인 

users = {딕셔너리} 


def login():
    user_id = input("ID를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")

    if user_id in users:
        if users[user_id] == user_password:
            current_user = {"id":user_id, "password": user_password}
            print("로그인 성공")
            return current_user
        else:
            print("비밀번호가 틀렸습니다.")
    else:
        print("사용자 정보가 없습니다.")
    return None

current_user = login()


# 로그아웃 
def logout(current_user):
    current_user = None 
    print("로그아웃이 완료되었습니다")
    return current_user


users = {}
def login():
    username = input("아이디를 입력하세요.")
    password = input("비밀번호를 입력하세요.")

    if username in users:
        if users[username] == password:
            current_user = {"username":username,"password":password}
            return current_user
        else:
            print("비밀번호가 틀렸습니다.")
    else:
        print("사용자 정보가 없습니다.")
        return None 
    
current_user = login()  

    
def logout(): 
    print("로그아웃 되었습니다.")
    return None

current_user = logout()
    
rented_by = [('책 번호', '책 제목','사용자이름'),('책 번호', '책 제목','사용자이름')......]


class Addbook:
    def __init__ (self):
        self.books = {}

    def add_book(self):
        book_title = input("책 제목을 입력해주세요.")
        book_number = input("책 번호를 입력해주세요.")
        self.books[book_title] = book_number
        print(f"'{book_title}' 도서가 등록되었습니다.")

book1 = Addbook()

book1.add_book()


class Deletebook:
    def __init__ (self):
        self.books = {}

    def delete_book(self):
        title_to_delete = None
        book_number = input("책 번호를 입력해주세요.")

        for title,number in self.books.items():
            if book_number == number:
                title_to_delete = title 
                break 

        if title_to_delete in self.books:
            self.books.pop(title_to_delete)
            print("도서가 삭제되었습니다.")
        else:
            print("존재하지 않는 책 번호입니다.")

book1 = Deletebook()

book1.delete_book = {"해리 포터": "001", "어린 왕자": "002"} #테스트용 책 추가

book1.delete_book()


#임의의 정수가 입력될 때 0이 나올 때 멈춰라. 
n = 1
while n != 0:
    n = int(input())
    if n!=0:
        print(n) 

#정수(1~100) 1개가 입력되었을 때 카운트다운을 출력해보다. 

n = int(input())

while n !=0:
    print(n)
    n = n-1 

#정수 1개 입력받아 카운트다운출력하기 2
n = int(input())

while n !=0:
    print(n-1)
    n = n-1





