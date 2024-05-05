def rat_con(r, unit, n, arr):
    if not arr:  # Check if the array is empty
        return -1
    else:
        total_food = 0
        for i in range(len(arr)):
            total_food += arr[i]
            if total_food >= r * unit:
                x = i + 1
                if x <= n:
                    return x
                else:
                    return 0
        return 0  # Return 0 if no valid number of houses found

r = 7
unit = 2
n = 8  # no. of houses
arr = [2, 8, 3, 5, 7, 4, 1, 2]

res = rat_con(r, unit, n, arr)

if res == -1:
    print("null array")
elif res == 0:
    print("insufficient food")
else:
    print("number of houses - ", res)