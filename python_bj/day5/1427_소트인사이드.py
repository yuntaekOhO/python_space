#배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
#첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
num = input()
num = list(num)
num.sort()
num.reverse()
for i in num:
    print(i,end="")


# num = int(input())
# num_list = list(map(int,list(str(num))))
# sorted_list = list(map(int,sorted(num_list,reverse=True)))  #sorted(대상리스트,역순지정)

# print(''.join(map(str,sorted_list)))