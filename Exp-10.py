#Code for Calculator 
#Coder : Aliya Shaikh 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."

print("---calculator---")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice = input("Enter your choice (1-4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input. Please enter a number between 1 and 4.")
  
'''
---calculator---
1. addition
2. subtraction
3. multiplication
4. division
Enter your choice (1-4): 2
Enter first number: 12
Enter second number: 23
12.0 - 23.0 = -11.0
'''
