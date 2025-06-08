
'''심희현'''

# 1. 학생 성적 관리 프로그램
'''
딕셔너리 활용 : 학생 이름을 키(key), 점수를 값(value)으로 저장
리스트 컴프리헨션 대신 반복문 : 조건에 맞는 학생 필터링,
sorted() 함수 : key=lambda x: x[1]로 점수 기준 정렬, reverse=True로 내림차순,
enumerate() : 순위 매기기에 활용,

주요 포인트:
sum(students.values())로 모든 점수의 합 계산
딕셔너리의 .items()로 (이름, 점수) 튜플 형태로 접근,
람다 함수 lambda x: x[1] 로 튜플의 두 번째 요소(점수) 기준 정렬
'''

class StudentGrades:
    def __init__(self, student_scores):
        self.student_scores = student_scores  # 학생 이름과 점수 딕셔너리

    def total_score(self):
        total = sum(self.student_scores.values())  # 모든 점수 합계
        return total

    def average_score(self):
        total = self.total_score()
        count = len(self.student_scores)  # 학생 수
        avg = total / count
        return avg

    def print_students_above_80(self):
        print("80점 이상인 학생들:")
        for name, score in self.student_scores.items():
            if score >= 80:
                print(name, score, "점")

    def sort_students_by_score(self):
        # 점수 내림차순 정렬 (기본은 True)
        sorted_list = sorted(self.student_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_list

    def print_ranking(self):
        sorted_students = self.sort_students_by_score()
        print("학생 성적 순위:")
        rank = 1
        for name, score in sorted_students:
            print(rank, "등", name, score, "점")
            rank += 1


# 2. 1의 갯수 반환
'''문제설명: 주어진 리스트의 값 중 1의 갯수를 반환하는 solution 함수를 완성해주세요'''
def solution(numbers):
    count = 0
    for num in numbers:
        count += str(num).count('1')
    return count






'''김가영'''
# 1. 홀수의 평균 구하기,
'''정수 n 이 주어질 때, n 이하의 홀수들의 평균을 구해서 return 하도록 solution 함수를 완성하세요.
[ 조건 ]
n은 1 이상의 자연수,
평균은 소수점 이하 첫째 자리까지 출력(소수점 자리 반올림),
[ 풀이 방식 ]
리스트 컴프리헨션과 sum()/ len()을 이용하여 구하기'''

def solution(n):
    number = [x for x in range(1, n+1) if x % 2 ==1]
    avg = sum(number)/len(number)
    return round(avg.1)

# 2. 최고 점수 학생 찾기
'''학생 이름과 점수가 담긴 딕셔너리 scores가 주어질 때, 가장 점수가 높은 학생의 이름을 return 하도록 solution 함수를 완성하세요.
[ 조건 ]
딕셔너리의 key는 문자열(이름), value는 정수(점수),
최고 점수를 받은 학생이 여럿일 경우 아무나 리턴,
[ 풀이 방식 ]
max() 함수와 lambda를 사용하여 구하기'''

scores = {"철수": 85, "영희": 92, "민수": 78, "영지": 88}
def solution(scores):
    return max(scores.items(), key = lambda x:x[1])[0] # (이름: 점수) -> [0] 이름 꺼내기
    






'''정효은'''
# 문제 1. 학생 성적 관리 시스템 (중급 난이도)
# 학생의 이름과 성적을 저장하고, 평균 점수를 계산하는 클래스를 작성하시오.

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_info(self):
        average = self.get_average()
        return f"이름: {self.name}, 평균 점수: {average:.1f}"
    


# 문제2.우편 번호 정렬
'''문제 설명: 각 주소가 담긴 배열과 우편번호 목록이 딕셔너리 형태로 주어질 때에서
오름차순 순서대로 주소를 정렬하는 코드를 작성해주세요.

* 제한사항
- 63002 ≤ 우편번호 ≤ 63364
- 우편번호는 항상 '시 - 동 - 길' 순으로 주어집니다. 예외사항은 없습니다.
- 같은 동은 주어지지 않으며, 같은 우편번호도 주어지지 않습니다.'''
def sort_addresses_by_zip(addresses, zip_codes):
    return sorted(addresses, key=lambda addr: zip_codes[addr])






'''배주완'''
#문제1. 간단한 은행 계좌 클래스

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 

    def deposit(self, money):
        self.balance += money  

    def withdraw(self, money):
        if money > self.balance:
            print("잔액 부족")  
        else:
            self.balance -= money

    def check_balance(self):
        print(f"잔액은 {self.balance}원입니다.") 



#문제2. 장바구니
class ShoppingCart:
    def __init__(self):
        self.items = []  

    def add_item(self, item_name, price):
        self.items.append({"name": item_name, "price": price})  

    def show_items(self):
        for item in self.items:
            print(f"{item['name']}: {item['price']}원")  

    def total_price(self):
        total = sum(item['price'] for item in self.items)
        print(f"총 가격은 {total}원입니다.")  
    

'''최은빈'''
'''1번'''
#반복문 사용
def solution_loop(n):
    total = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            total += i
    return total

#sum range 사용
def solution_sum(n):
    return sum(range(0, n + 1, 2))


'''2번'''
#count()
def solution(array, n):
    return array.count(n)

#collections.Counter
from collections import Counter

def solution(array, n):
    counter = Counter(array)
    return counter.get(n, 0)

