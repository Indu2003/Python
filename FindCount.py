def findCount(arr, length, num, diff):
    count = 0  
    for i in range(length):
        if abs(arr[i] - num) <= diff:  
            count += 1
    return count

arr = [12, 3, 14, 56, 77, 13]
length = len(arr)
diff = 2
num = 13
result = findCount(arr, length, num, diff)
print("No.of elements within the range:", result)
