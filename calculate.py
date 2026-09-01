#steps to build 
# 1. function to perform operation 
#2. user input 
# 3. print result 

def add(a, b):
    return a + b;

def subtract(a, b):
    return a - b;
def multiply(a, b):
    return a * b;
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b;
def avg(a, b):
    return (a + b) / 2;



print("Select operation:\n" ,"1. Add\n ","2. Subtract\n","3. Multiply\n", "4. Divide\n ", "5. Average")

select = int(input("Enter choice (1,2,3,4,5): "))
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))

if select == 1:
    print(input1, "+", input2, "=", add(input1, input2))
elif select == 2:
    print(input1, "-", input2, "=", subtract(input1, input2))
elif select == 3:
    print(input1, "*", input2, "=", multiply(input1, input2))
elif select == 4:
    print(input1, "/", input2, "=", divide(input1, input2))
elif select == 5:
    print("Average of", input1, "and", input2, "is", avg(input1, input2))
else:
    print("Invalid choice. Please enter a valid option (1-5).")