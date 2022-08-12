print("Hello, World!")
a = 3
b = 4
# / 나누기 , // 몫 ,  % 나머지 , ** 제곱
print(a+b)

#포맷팅
#%s = 문자열, %c = 문자1개, %d = 정수, %f = 부동소수, %o = 8진수, %x = 16진수, %% = '%' 자체
a = "I eat %d apples." % 3
print(a)

#여러개인 경우 괄호로 묶음
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)
# format() : {}에 지정한 문자열 넣기
a = "asdfasdf efewfsf vsgsejijif {} sadfasdf".format("안녕")
print(a)
b = "esekfosek {age}살 {name} emfsiefm".format(name="홍길동",age=13)
print(b)
#3.6버전 이상 지원
name = "장영실"
a = f"나의 이름은 {name}입니다."
print(a)
#소숫점 자리수, 문자열도 공백으로 띄움
a = "%0.4f" % 3.123414
print(a)
b = "%10s마바사" % "가나다라"
print(b)

#문자열 개수 세기(count), 위치 알려주기(find)(가장 먼저나온 위치만)
a = "hobby"
print(a.count('b')) # 문자열에 지정한 문자 개수 반환, 없으면 0
print(a.find("a")) # 문자열에서 지정한 문자의 인덱스 반환, 없으면 -1
print(a.index("o")) # o의 인덱스 반환, 없으면 에러

#문자열 삽입 (join)
a  = ","
print(a.join("abcdef"))

#대소문자 변환
a = "abcd"
print(a.upper())
b = "ABCD"
print(b.lower())

#공백지우기 (strip)
a = "       HI "
print(a.strip())

#문자열 바꾸기(replace)
a = "Life is too short"
print(a)
#              타겟    대체할 문자
a = a.replace("Life", "Your leg")
print(a)

#문자열 나누기(split)
a = "Life is too short"
print(a.split()) #공백을 기준으로 나누기
a = "1:2:3:4"
print(a.split(":")) #지정한 문자를 기준으로 나누기

