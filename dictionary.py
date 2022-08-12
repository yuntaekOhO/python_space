#키=값 형태 , map,hash,json과 같은 개념
#연관 배열 또는 해시, key를 통해 value를 얻는다

#값 얻기 [], get() 둘 다 key로 값을 얻음
dic = {'name':'Eric', 'age':15}
# []
print(dic['name']) # Eric : key인 name으로 값 Eric 출력
print(dic['age']) # 15 : key인 age로 값 15 출력
print(dic) # {'name': 'Eric', 'age': 15} : 전체 출력
# get()
print(dic.get('name'))

# 없는걸 얻으려고 하면 [] 방식은 에러 발생
# get() 방식은 None 출력
print(dic.get('dic')) # None
print(dic.get('dic','없음')) # 없음 : None 대신 출력 될 default 값 지정

#딕셔너리에 key:value 추가
a = {1:'a'}
a['name'] = "익명"
print(a) #{1: 'a', 'name': '익명'} - key(name),value(익명)이 추가됨

#삭제
del a[1] # []안에는 key임
print(a) # {'name': '익명'}

#주의사항 : key는 중복될 수 없음 : 해당하는 key에 뒤에나온 value를 덮어 씌움
a = {1:'a',1:'b'}
print(a) #{1: 'b'}

#튜플 형태로 -
# key 목록 얻기 (keys)
a = {1:'홍길동', 2:'이순신', 3:'장영실'}
print(a.keys()) # dict_keys([1, 2, 3])
# value 목록 얻기 (values)
print(a.values()) # dict_values(['홍길동', '이순신', '장영실'])
# key-value 쌍으로 목록 얻기
print(a.items()) # dict_items([(1, '홍길동'), (2, '이순신'), (3, '장영실')])
#아래의 형태로 많이 쓰임
for k in a.keys():
    print(k)
for k,v in a.items():
    print("키는: " + str(k))
    print("밸류는: " + v)


#모두 지우기
a.clear()
print(a)

# key 포함 여부
print('phone' in a) # False : a에 phone이라는 key가 있는지 체크 (true,false)
print('name' in dic) # True : dic에 name이라는 key 있는지 체크