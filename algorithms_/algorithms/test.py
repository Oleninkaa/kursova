
arr1 = [1,2,3,4,5]
arr2 = [11,12,13,14,15]
start=2
finish = 4

temp = arr1[start:finish]
arr1[start:finish] = arr2[start:finish]
arr2[start:finish] = temp
print(arr1, arr2)