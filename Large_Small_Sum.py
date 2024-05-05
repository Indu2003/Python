def LargeSmallSum(arr):
    temp_even=[]
    temp_odd=[]
    for i in range(len(arr)):
        if(arr[i]%2==0):
            temp_even.append(arr[i])
        else:
            temp_odd.append(arr[i])
    return temp_even,temp_odd

arr=[3,2,1,7,5,4]

temp_even,temp_odd=LargeSmallSum(arr)


s1 = sorted(temp_even)
s2 = sorted(temp_odd)

result=s1[len(s1)-1]+s2[1]
print(result)

    