#조건문 if 
#들여쓰기 철저하다
money = True
if money:
    print('택시 타')
else:
    print('걸어 가')

if money:
    pass # 아무것도 하지 않음
else:
    print('걸어 가')

# 다중 조건문 : if ~ elif ~ else
pocket = ['paper','cellphone']
card = True
if 'coin' in pocket:
    pass
elif card:
    print('타고 가')
else:
    print('걸어 가')

#조건부 표현식
score = 70
#if score >= 60:
#    message = "success"
#else:
#    message = "failure" 를 아래처럼 표현
message = "success" if score >= 60 else "failure"
print(message)