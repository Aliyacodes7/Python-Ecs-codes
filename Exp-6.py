#Code for pattern generation
#Coder:Aliya Shaikh

row=int(input("enter the number of rows:"))
for row in range(1,row+1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

"""
OUTPUT:
enter the number of rows:5
* 
* * 
* * * 
* * * * 
* * * * * 
"""
