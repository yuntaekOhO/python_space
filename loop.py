#while문 break, continue 가능
#반복 조건으로 bool형 사용
# >, <, <=, >=, ==, and, or, &, |, in, not, True, False
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다' % treeHit)
    if treeHit == 10:
        print('나무가 쓰러졌습니다')
        

#for문
list = ['one','two','three']
for i in list: # list 자리에는 리스트,튜플,문자열
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    #print(str(first) + " " + str(last)) : 문자열 숫자열 혼용
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


#range(?,?)
sum = 0
for i in range(1,11): # 1 이상 11미만 : 1~10의 합
    sum = sum + i
print(sum)

#2중 for문
for i in range(2,10):
    for j in range(1,10):
        # end=" " -> 개행을 막음, default:\n
        print(i*j, end=" ")
    print('')