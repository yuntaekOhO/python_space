#list는 배열과 같다
odd = [1,3,5,7,9]
a = []
b = [1,2,3]
c = ['Life','is','to','short']
d = [1,2,['Save','Earth'],4] #여러 타입을 같이 쓸 수 있고, 리스트안에 리스트(2차원)도 가능
n = [1,2,3,4,5,6]
#전체 출력
print(odd)
print(d[2]) # ['Save', 'Earth']
print(d[2][1]) #Earth

#리스트의 슬라이싱
print(n[0:2]) # [1, 2] : 리스트의 0이상 2미만 출력
print(n[:4]) # [1, 2, 3, 4] : 리스트의 시작부터 4번 인덱스 미만 출력
print(n[2:]) # [3, 4, 5, 6] : 리스트의 2번 인덱스부터 끝까지 출력

#리스트끼리의 더하기
print(b + c) # [1, 2, 3, 'Life', 'is', 'to', 'short']
print(b * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 값 변경
b[0] = 99
print(b) # [99, 2, 3]

b[1:] = [98, 97]
print(b) # [99, 98, 97]

#리스트 삭제
b[0:2] = []
print(b) # [97]

#del
a = ["손흥민","황희찬","황의조"]
del a[0]
print("del",a) # ['황희찬', '황의조']

#리스트에 제일 마지막 요소로 추가 (append)
n.append(7)
print(n) # [1, 2, 3, 4, 5, 6, 7]

#리스트 정렬 (sort, reverse)
n.reverse()
print(n) # [7, 6, 5, 4, 3, 2, 1]
n.sort()
print(n) # [1, 2, 3, 4, 5, 6, 7]

#지정한 요소가 몇번째 인덱스에 있는지 반환
print(a.index("황의조")) # 1 , 없으면 에러  ValueError: '이재성' is not in list 

#특정 인덱스에 요소 추가
a.insert(0,"손흥민") # 0번 인덱스에 6 추가
print(a)

#특정 요소 삭제(remove)
a.remove("황의조")
print(a)
n.remove(4) # 4는 인덱스가 아닌 값임, 4라는 요소가 여러개일 경우 가장 처음의 4만 삭제
print(n)

#리스트 요소 뒤에서부터 추출(pop)
print(n.pop())

#리스트에 지정한 값이 몇개인지 반환(count)
m = [1,1,1,2,3,2,1,1,3,3]
print(m.count(1)) # 5

#리스트에 리스트 형태로 추가 (extend)
n.extend(m)
print(n) # [1, 2, 3, 5, 6, 1, 1, 1, 2, 3, 2, 1, 1, 3, 3] 

ex = [0] * 10
ex[0] = 1
print('ex :', ex)