n = 5
arr = [0, 9, 3, 5, 1, 2]
s1 = sorted(arr)
DP = sum(arr)
SP = 0

while SP < DP:
    modi_DP = DP - arr[n - 1]
    print("Damon power decreased...")
    SP = SP + arr[n - 1]  # Changed from arr[n] to arr[n-1]
    print("Stephen power:", SP)
    n = n - 1
    if n < 0:  # Check if n becomes negative (end of array)
        print("Cannot solve")
        break  # Exit the loop if n is negative

# If the loop exits without printing "Cannot solve", it means SP >= DP
else:
    print("Damon's power is less than or equal to Stephen's power.")
