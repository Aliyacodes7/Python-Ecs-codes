#Code for factorial
#Coder:Aliya Shaikh

n=int(input("enter the number:"))
fact=1
if(n>0):
    for i in range(1,n+1):
        fact=fact*i
        print(f"value of the factorial is:", fact)
else:
    print("factorial does not exist")

"""
OUTPUT:
enter the number:8
value of the factorial is: 1
value of the factorial is: 2
value of the factorial is: 6
value of the factorial is: 24
value of the factorial is: 120
value of the factorial is: 720
value of the factorial is: 5040
value of the factorial is: 40320
"""
