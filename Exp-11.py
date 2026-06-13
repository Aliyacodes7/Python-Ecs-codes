#Code for handling basic exception 
#Coder : Aliya Shaikh 

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric value")

'''
Enter the first number: 23
Enter the second number: 45
Result: 23.0 / 45.0 = 0.51111111
'''
