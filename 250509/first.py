#튜플 
'''[특징] 
- 한 번 만들면 변하지 않는다. (불변성)

- 튜플은 읽기만 가능하다. 
crud(create, read, update, delet)

- 리스트보다 기능이 적다. (제한적이다)
- 튜플 안에 튜플을 넣을 수 있다. 
- 중복을 허용한다. 
- 추가 제거, 수정 불가능하다?'''



#set 자료구조 
'''
- 중복을 허용하지 않는다.
- 형변환 list -> set
- set은 인덱스 기능이 먹히지 않는다. 
- 집합을 사용할 때 교집합 또는 합집합 -> set
- 합집합 | 
- 교집합 &
- 리스트나 튜플에서는 합집합과 교집합을 사용할 수 없다. 
- 알고리즘 문제에서 많이 사용된다. 
- 순서를 보장하지 않는다. 
- 수정이 가능하다. 
- 추가할 때 add를 사용한다. 
- 지울때는 remove를 사용한다. 
- 없는 항목은 지울 수 없다. 

왜 활용할까?

'''
a = [1,1,1,2,2,3]
b = set(a)
print(b)
c = list(b)

a = {1,2,3}
print(a[0])

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
#각각 중복된 것은 없다. 
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}") # 기준은 왼쪽이다. 공통분모포함 오른쪽의 항목을 제거함. 
print(f"차집합: {set2 - set1}")

a = {1,2,3}
d = {"a", 1,2,3,1,"a"}

e = list(d)
print(e)

#set수정
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.add('orange')
fruits.add('orange')
print(fruits)

fruits.remove('apple')
print(fruits)
fruits.remove('apple') # keyerror: apple

print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

#딕셔너리 dict()

# key: value 
my_dict = {"me":"길동"}
my_dict2 = dict()
my_dict2_1 = dict([("one":"하나"),('two','둘')])
print(my_dict2_1)

my_dict3 = {'me' :[1,2,3],"me2" : "good"}

print(my_dict)

# 데이터 추가 
dict4 = dict()
dict4["max"] = [1,2,3,4] #데이터 삽입 {'max': [1,2,3,4]}
print(dict4)

# 문자열로 하는게 일반적이다. 
# 딕셔너리 벨류에는 딕셔너리 안에 또 딕셔너리를 넣을 수 있다. 

#데이터 읽기 
a = dict4["max"]

dict_1 = dict()
dict_1 =


person = {'name' : 'licat', 'age':25, 'height':165.5}
print(f"이름은 :{person["name"]}입니다.")
print(f"나이는 :{person["age"]}입니다.")

#키 값이 없는데 가져오면 어떻하지?
#print(f"생년월일은 : {person["good"]}") keyError : 'good'
# 키에 들어가서 벨류의 값을 찾고 그 값을 바꿔야 한다. 

#데이터 수정
person["age"] = 30
print(person)

person = {'name': 'licat', 'age': 25, 'height': 165.5}
person['height'] = 170
person['weight'] = 50
print(person)

#데이터 삭제 
del person["height"]
print(person)
person["age"] = None #키를 남기고 값을 없애고 싶을 때 

b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
b = {"good1": {"good2": [1, 2, 3, [1, 2, 3, 4]]}}

b["good1"]["good2"][3].append(4)
pring(b)

#딕셔너리로 최상위, 최하위 구조를 만들 수 있다. 

# get(키,키가 없을 경우의 value)
city = person.get('city',"없는뎅")
print(city)
city2 = person.get('city2',"없는뎅")
print(city2)

person ={"name":"licat","age":25,"city":"seoul"}
#키만 가져온다. 

person_key = person.keys() #키 값들만 추출
print(person_keys) #dict_keys(['name', 'age', 'city'])
a = list(person_keys) #형변환
print(a) 

#value만 추출
person_calues = person.values() #밸류 값들만 추출 
peirn(person_values) #dict_values(['licat', 25, 'seoul'])
b = list(person_calues)
print(b)

#전체를 추출 

