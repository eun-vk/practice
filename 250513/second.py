
# 로그인 

'''users = {딕셔너리} 


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

# 책 추가 
class Bookmanager:
    def __init__ (self):
        self.books = {}

    def add_book(self):
        book_title = input('추가할 책 제목을 입력하세요.')
        book_number = input('책 번호를 입력해주세요.')

        if book_number in self.books.values():
            print("이미 등록된 책 번호입니다.")
            return
        
        self.books[book_title] =book_number
        print(f"{book_title} 책이 추가되었습니다.")

    def delete_book(self):
        title_to_delete = None 
        book_number = input("삭제할 책 번호를 입력하세요.")

        for title,number in self.books.items():
            if book_number == number:
                title_to_delete = title
                break 

        if title_to_delete is not None:
            self.books.pop(title_to_delete)
            print (f"{title_to_delete}가 삭제되었습니다.")
        else:
            print ("존재하지 않는 책 번호입니다.")


문제: MovieManager클래스 만들기 
'''
아래 조건에 맞는 MovieManager 클래스를 작성하세요.

__init__()에서 영화 목록을 저장할 딕셔너리 movies를 만든다.

add_movie() 메서드

사용자에게 영화 제목과 영화 ID를 입력받는다.

이미 등록된 영화 ID가 있으면 "이미 등록된 영화 ID입니다."를 출력하고 추가하지 않는다.

중복이 아니면 딕셔너리에 영화 제목과 ID를 저장하고 "영화 제목이 추가되었습니다."를 반환한다.

delete_movie() 메서드

사용자에게 삭제할 영화 ID를 입력받는다.

해당 ID가 있으면 그 영화 제목을 삭제하고 "영화 제목이 삭제되었습니다."를 반환한다.

없으면 "존재하지 않는 영화 ID입니다."를 반환한다.
'''

class MovieManager:
    def __init__ (self):
        self.movies = {}

    def add_movie(self):
        movie_title = input("영화제목을 입력하세요.")
        movie_ID = input("영화ID를 입력하세요.")

        if movie_ID in self.movies.values():
            print("이미 존재하는 ID입니다. ")
            return 
        
        self.movies[movie_title] = movie_ID
        print(f"{movie_title}이 추가되었습니다.")

    def delete_movie(self):
        title_to_delete = None
        movie_ID = input("삭제할 영화 ID를 입력해주세요.")

        for title, ID in self.movies.items():
            if movie_ID == ID:
                title_to_delete = title
                break
            
        if title_to_delete is not None:
            self.movies.pop(title_to_delete)
            print(f"{title_to_delete} 영화가 삭제되었습니다.")

        else:
            print("존재하지 않는 영화 ID입니다. ")'''
        
        
import sys

class LibrarySystem:
    def __init__(self):
        self.users = {}  # 사용자 정보 저장용 딕셔너리
        ###########
        self.current_user = None # 현재 로그인 한 사용자
        ###########

        ###########
        # 도서 관리
        self.books = [] # {"title": str, "rented_by": str or None}
        ###########

    # ------------------------ 회원관리 ------------------------
    def signup(self):  # 회원가입 함수
        while True:
            username = input("아이디를 입력하세요: ")

            if username in self.users:
                print("❗ 이미 존재하는 아이디입니다.")
            else:
                break

        password = input("비밀번호를 입력하세요: ")

        self.users[username] = password

        print(f"🎉 {username}님, 회원가입이 완료되었습니다!")


    def login(self):  # 로그인 함수
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"✅ {username}님, 로그인 성공!✅")
            return True
        else:
            print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")
            return False

    def logout(self):
        answer = input("로그아웃 하시겠습니까? [1.네 / 2.아니요] ")
        if answer == "1":
            print("로그아웃 되었습니다.")
            self.current_user = None
            return True
        elif answer == "2":
            print("로그아웃을 취소했습니다.")
            return False
        
    # ------------------------ 도서관리 ------------------------
    def add_book(self):
        title = input("책 제목을 입력해주세요: ")
        self.books.append({"title": title, "rented_by": None})
        print(f"'{title}' 도서가 등록되었습니다.")

    def delete_book(self):
        self.show_books()
        try:
            index = int(input("삭제할 책 번호를 입력해주세요: ")) - 1
            if 0 <= index < len(self.books):
                removed = self.books.pop(index)
                print(f"'{removed['title']}' 도서가 삭제되었습니다.")
            else:
                print("존재하지 않는 책 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def show_books(self):
        print("\n[전체 도서 목록]")

        ###########
        if not self.books:
            print("📂 등록된 도서가 없습니다.")
            return
        ###########
        
        for i, book in enumerate(self.books, 1):
            status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
            print(f"{i}. {book['title']} / {status}")

    def search_books(self):
        if self.current_user is None:
            print("로그인 후 이용해주세요.")
            return
        keyword = input("검색할 책 제목 또는 키워드를 입력하세요: ").lower()
        found = False
        print("[검색 결과]")
        for i, book in enumerate(self.books):
            if keyword in book["title"].lower():
                status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
                print(f"{i+1}. {book['title']} - {status}")
                found = True
        if not found:
            print("검색된 책이 없습니다.")

    # ------------------------ 대여/관리 ------------------------
    def rent_book(self):
        self.show_books()
        try:
            index = int(input("대여할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books):
                book = self.books[index]
                if book["rented_by"] is None:
                    book["rented_by"] = self.current_user
                    print(f"'{book['title']}' 책이 대여되었습니다.")
                else:
                    print("이미 대여 중인 책입니다.")
            else:
                print("존재하지 않는 책 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def return_book(self):
        user_books = [(i, b) for i, b in enumerate(self.books) if b["rented_by"] == self.current_user]
        if not user_books:
            print("반납할 책이 없습니다.")
            return
        print("[내가 대여한 책 목록]")
        for i, book in user_books:
            print(f"{i+1}. {book['title']}")
        try:
            index = int(input("반납할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books) and self.books[index]["rented_by"] == self.current_user:
                self.books[index]["rented_by"] = None
                print(f"'{self.books[index]['title']}' 책이 반납되었습니다.")
            else:
                print("해당 책은 당신이 대여한 책이 아닙니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def extend_books(self):
        user_books = [(i, b) for i, b in enumerate(self.books) if b["rented_by"] == self.current_user]
        if not user_books:
            print("연장할 책이 없습니다.")
            return
        print("[연장 가능한 책 목록]")
        for i, book in user_books:
            print(f"{i+1}. {book['title']}")
        try:
            index = int(input("연장할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books) and self.books[index]["rented_by"] == self.current_user:
                print(f"'{self.books[index]['title']}' 연장 완료")
            else:
                print("당신이 대여한 책이 아닙니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    # ------------------------ 메인/메뉴 ------------------------
    def menu(self):
        print("\n[도서관 시스템 메뉴]")
        print("1. 도서 목록 보기")
        print("2. 책 추가하기")
        print("3. 책 삭제하기")
        print("4. 책 대여하기")
        print("5. 책 반납하기")
        print("6. 대여 연장하기")
        print("7. 책 검색하기")
        print("0. 로그아웃 및 종료")

        ###########
        try:
            choice = int(input("메뉴를 선택하세요: "))
            if 0 <= choice <= 7:
                return choice
            else:
                print("0부터 7 사이의 숫자를 입력해주세요.")
                return None
        except ValueError:
            print("숫자를 입력해주세요.")
            return None
        ###########
        # return input("메뉴를 선택하세요: ")

    def main(self):
            while True:
                choice = self.menu()
                #################
                if choice is None:
                    continue
                #################

                if choice == 1:
                    self.show_books()
                elif choice == 2:
                    self.add_book()
                elif choice == 3:
                    self.delete_book()
                elif choice == 4:
                    self.rent_book()
                elif choice == 5:
                    self.return_book()
                elif choice == 6:
                    self.extend_books()
                elif choice == 7:
                    self.search_books()
                elif choice == 0:
                    if self.logout():
                        break
                else:
                    print("잘못된 입력입니다.")

    def run(self):
        print("도서관 시스템에 오신 것을 환영합니다!")
        while True:
            print("\n1. 회원가입")
            print("2. 로그인")
            print("0. 종료")
            menu = input("메뉴를 선택하세요: ")
            if menu == "1":
                self.signup()
            elif menu == "2":
                if self.login():
                    self.main()
            elif menu == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

if __name__ == "__main__":
    system = LibrarySystem()
    system.run()




