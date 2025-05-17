'''# 진수 
x = ob110 
print(x)
print(type(x))'''

#translate 
table = str.maketrans('hello','jfmmo')
text = 'hello'
result = text.translate(table)
print(result)

# 리스트 실전 문제: 할 일 관리 앱 만들기 
'''당신은 할 일을 관리하는 앱을 만들고 있으며, 
사용자 입력을 기반으로 할 일 목록을 처리해야 합니다.'''

to_do = []

to_do.append('청소')
to_do.append('공부')
to_do.append('운동')

to_do.extend(['요리', '설거지'])

change = to_do.index('청소')
to_do[change] = '대청소'

to_do.insert(0,'대청소')

to_do.remove('요리')

result = to_do.pop(3)

count_study = to_do.count('공부')
index_study = to_do.index('공부')

to_do.sort()
to_do.reverse()
to_do_list = to_do.copy() 
to_do.clear()

print("복사된 할 일 목록:", to_do_list)
print("비워진 to_do:", to_do)



# 튜플 실전 문제: “기온 기록”
'''시나리오
일주일간의 최고기온을 튜플로 저장하고 분석합니다.'''

week_temps = (26, 27, 28, 27, 29, 30, 30)
temps_count = week_temps.count(27)
temps_index = week_temps.index(30)
temps_len = len(week_temps)
slicing = week_temps[3:6]
slicing_1 = week_temps[::-1]
result = list(week_temps)
result.append('강풍')
result_com = tuple(result)


# 딕셔너리 실전 문제: “직원 정보 관리”
'''
시나리오
회사에서 직원들의 정보를 딕셔너리로 관리합니다. 
키는 이름, 값은 부서입니다.
'''

unit = {'영희':'회계','철수':'영업'}
other_unit = {'나연':'디자인'}
unit.update({'민수':'인사'})
unit['민수'] = '인사'
unit['영희'] = '기획'
value_c = unit.get('철수')
minsu_unit = unit.pop('민수')
every_value = unit.values()
every_items = unit.items()
unit.setdefault('지민', '개발')
unit.update(other_unit)
new_unit = unit.copy()
unit.clear()

# 셋 실전 문제_동아리 신청 관리 시스템
'''
시나리오
중복 신청을 제거하고, 동아리별 인원을 관리합니다.
'''
중복신청리스트 = ['영희', '철수', '민수', '영희', '수지']

dupReqs = set(중복신청리스트)
dupReqs.add('지민')
dupReqs.remove('철수')
'민수' in dupReqs
dupReqs.discard('태형')
people = dupReqs.pop()
dupReqs1 = dupReqs.copy()
dupReqs.clear()

set1 = {"영희", "철수", "지민"}
set2 = {"지민", "나연", "정국"}

print(dupReqs.union(set1))  # print(a | b) 
print(dupReqs.difference(set2)) # print(a - b)
print(dupReqs.intersection(set1)) # print(a & b) 
dupReqs.update(set2)




