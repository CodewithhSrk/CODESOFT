#INPUT
a = float(input("Enter The First Number: "))
b = float(input("Enter The Second Number: "))
operator = input("Select Calculation  (+, -, *, /): ")

#FUNCTION
def calculate(a, b, operators):   
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b 
    elif operator == '/':
        if b!= 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

#CALLING PARAMETERS
results = calculate(a, b, operator)
print("ANS: ", (results))