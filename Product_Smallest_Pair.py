def ProductSmallestPair(sum,arr):
    n=len(arr)
    if n==None or n<2:
        return -1
    else:
        smallest = float('inf')
        second_smallest = float('inf')
        for i in range(n):
            if arr[i] <= smallest:
                second_smallest = smallest
                smallest = arr[i]
            elif arr[i] <= second_smallest:
                second_smallest = arr[i]
        if smallest + second_smallest <= sum:
            return smallest * second_smallest
        else:
            return 0
                      
arr=[9,8,3,-7,3,9]
sum=4
result=ProductSmallestPair(sum,arr)
print(result)
               

