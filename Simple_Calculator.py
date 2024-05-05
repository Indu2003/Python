def add (x,y):
    return x+y
def sub(x,y):
     return x-y
def mult(x,y):
     return x*y
def div(x,y):
    if (y==0):
          print("diision by zero is not allowed")
    else:
         return x/y
    
print("select operation : ")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")

choice=input("enter choice 1/2/3/4 : ")
n1=float(input("enter the number 1 : "))
n2=float(input("enter the number 2 : "))

if choice =='1':
      print(n1 ,"+", n2,"=",add(n1,n2))
elif choice =='2':
      print(n1 ,"-", n2,"=",sub(n1,n2))
elif choice =='3':
      print(n1 ,"*", n2,"=",mult(n1,n2))
elif choice =='4':
      print(n1 ,"/", n2,"=",div(n1,n2))
else :
     print("Invalid...")
         