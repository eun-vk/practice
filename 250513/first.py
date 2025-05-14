
#딕셔너리 
# dic_test = {'노래제목': '아무노래', '가수':'지코','날짜':'2020.01.13'}

'''dic_test = {"노래제목":"아무노래"}
dic_test["가수"] ="지코" # 정보 추가 시 대괄호 사용


dic_test["날짜"] = "2020.01.13"


#딕셔너리 삭제 del 
dic_test = {'노래제목': '아무노래', '가수':'지코','날짜':'2020.01.13'}

del dic_test["날짜"] '''


# 값 가져오기 -> 변수[key]
'''dic_test = {'노래제목': '아무노래', '가수':'지코','날짜':'2020.01.13'}

print(dic_test['노래제목'])

# get(key)
# 딕셔너리면[key] vs 딕셔너리명.get(key)

키 값이 없을 때 다른다. 딕셔너리명[key]는 오류, get은 None 빈 값 출력 '''


# 키 값만 가지고 오고 싶을 때 keys()
dic3 ={'name': 'mh','age': 20, 'phone':'010-123-4567'}
print(dic3.keys())

print(list(dic3.keys()))


# 값만 가지고 오고 싶을 때 values()
print(list(dic3.values()))

# for문 활용 
for key in dic3.keys():
    print(key)

# items() key와 values 함께 받아오기 
for key, value in dic3.items():
    print(key, value)


# setdefault 
'''
키값이 딕셔너리에 있으면 키값을 반환하고 키값이 없으면 딕셔너리에 추가되어 반환된다. 
'''
# update 기존 딕셔너리에 추가 데이터를 병합

#set 
'''
- 중복 값을 허용하지 않는다. 
- 순서가 있는 자료가 아니다. 
- 인덱싱 안된다.
- 중복되는 문자열을 제거한다.  
'''
#set의 메서드 
#add 
set1 ={1,2,3}
set1.add(4)
print(set1)

#clear
setq ={1,2,3,4}
set1.clear()
print(set1)

#copy()
set1:{1,2,3}
set2 = set1.copy()
print(set2)

#remove() 특정 값을 지워라 
set = (1,2,3,4)
set1.remove(3)
print(set1)

#discard() 특정 값을 지우려는데 없어도 에러가 안난다. 

#pop 값을 지운다. 

#difference(others) 다른 집합과의 차집합을 구함. 
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.difference(set2))

#intersection(others) 교집합
#isdisjoint(other) 두 집합이 공통 원소를 가지지 않으면 True를 반환
#issubset(other) 집합이 other의 부분집합인 경우 True를 반환
#issuperset(other) 집합이 other의 상위집합인 경우 True를 반환
#union(others) 모든 others집합과의 합집합을 반환

#연습문제
#1번
student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}

sum(student_score.values())