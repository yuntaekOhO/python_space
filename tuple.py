#튜플은 값 수정, 길이 변경 불가능
#튜플은 변하지 않는다
t1 = (1,2,'a','b')
#del t1[0] 에러
print(t1)
#인덱싱, 슬라이싱으로 조회는 가능
print(t1[1]) # 2
print(t1[0:3]) # (1, 2, 'a')

t2 = (3,4)
#새로운 튜플이 만들어진 것
print(t1 + t2) #(1, 2, 'a', 'b', 3, 4) 
print(t1 * 3) #(1, 2, 'a', 'b', 1, 2, 'a', 'b', 1, 2, 'a', 'b')