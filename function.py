#함수 정의
def sum(a, b):
    result = a + b
    return result
print(sum(1,4))

#여러개의 인자 가변적으로 정의
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))
print(sum_many(1,2,3,4,5,6,7,8,9,10))

#keyword argument (dictionary)
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 : " + kwargs[k])
print_kwargs(name='홍길동',age='25')

#인자의 기본값 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자")
    else:
        print("여자")
say_myself("우영우",20,False)
say_myself("홍길동",22)