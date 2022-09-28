import copy

temp = [[1,2,3,4],[4,3,2,1],[1,2,1,6]]
result = [item[:] for item in temp]

arr = copy.deepcopy(temp)

arr[0] = [9]
temp.append([1,1,1,1])
result[1][1] = 4

print(temp)
print(result)
print(arr)

def exam(a):
    print(a)
arr1 = list()
# print(arr1)
exam(arr1)

exam1 = list()
print('list()로 선언만 한 리스트 길이',len(exam1))