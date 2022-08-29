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

# sorted( <list> , key=<function> , reverse=<bool> )
# : 원본 내용을 바꾸지 않고, 정렬한 값을 반환
#   List, Tuple, Dictionary, str에 모두 사용 가능
#   key 속성을 통하여 정렬할 기준을 정할 수 있다.
#   reverse 속성이 True면 내림차순, False면 오름차순으로 정렬. (Default-False)
arr = [10, 40, 20, 15]
#arr = sorted(arr, reverse=True)
print("sorted() :" , sorted(arr, reverse=True))
print("arr :",arr)

# <list>.sort(key=<function>, reverse=<bool>)
# : 원본 자체를 수정한다
#   반환값은 None
#   Tuple, Dictionary, str은 사용 불가