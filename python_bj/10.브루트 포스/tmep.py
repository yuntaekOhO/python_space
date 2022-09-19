import copy

temp = [[1,2,3,4],[4,3,2,1],[1,2,1,6]]
result = temp

arr = copy.deepcopy(temp)


arr[0] = [9]
temp.append([1,1,1,1])
result.append([2,2,2,2])


print(temp)
print(result)
print(arr)