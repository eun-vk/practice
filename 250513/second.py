
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
        self = books ={}

    def delete_book(self):
        delete_for_book = 0
        book_number = input("책 번호를 입력해주세요.")
        for (number,title) in books:
            if book_number == 