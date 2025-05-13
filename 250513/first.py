
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
    prin(key)

# items() key와 values 함께 받아오기 
for key, value in dic3.items():
    print(key, value)


# for문 
