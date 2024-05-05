def differenceofSum(n,m):
    Snd = 0
    Sd=0
    for i in range(1,m+1):
        if i%n==0:
            Snd+=i
        else:
            Sd+=i
    return Snd,Sd
n=int(input("enter the divisor: "))
m=int(input("enter the ending number : "))
Snd,Sd=differenceofSum(n,m)
result = Sd-Snd
print("the  difference : ",result)