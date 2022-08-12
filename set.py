#집합, set
#집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
#중복을 허용하지 않는다
#순서가 없다
s1 = set([1,2,3])
print(s1) # {1, 2, 3}

s2 = {4,5,6}
print(s2) # {4, 5, 6}

l = [1,2,2,3,3,3]
newList = list(set(l))  # 중복값이 있는 리스트를 set을 이용해 중복값을 제거하고 다시 리스트로 만듦
print(newList) # [1, 2, 3]

s3 = set("Hhello") # 문자열 set 가능 대소문자 개별로 봄, 순서 없음
print(s3) # {'o', 'h', 'e', 'H', 'l'}

#교집합 1 : &
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) # {4, 5, 6}

#교집합 2 : intersection()
s3 = s1.intersection(s2) 
print(s3) # {4, 5, 6}

#합집합 1 : |
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
#합집합 2 : union()
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합 : -
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 9, 7}
#차집합 : difference()
print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {8, 9, 7}

#값 1개 추가 add
s1 = set([1,2,3])
s1.add(4)
print(s1) # {1, 2, 3, 4}
#값 여러개 추가 update
s1.update([5,6,7,8,9])
print(s1) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#특정 값 제거 remove
s1.remove(2)
print(s1)
