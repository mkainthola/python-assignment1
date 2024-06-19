# Program that acts as a simple calculator. (It should take two numbers and an operator (+, -, *, /) as input and print the result)
def calculate(num1, num2, operator): 
    if operator == '+': 
        return num1 + num2 
    elif operator == '-': 
        return num1 - num2 
    elif operator == '*': 
        return num1 * num2 
    elif operator == '/': 
        if num2 == 0: 
            return "Error: Division by zero is not allowed." 
        else: 
            return num1 / num2 
    else: 
        return "Error: Invalid operator." 
def main(): 
    try: 
        num1 = float(input("Enter the first number: ")) 
        num2 = float(input("Enter the second number: ")) 
        operator = input("Enter the operator (+, -, *, /): ") 
        result = calculate(num1, num2, operator) 
        print(f"\nResult: {result}") 
    except ValueError: 
        print("Error: Please enter valid numbers.") 
    except Exception as e: 
        print(f"Error: {e}") 
if __name__ == "__main__": 
    main() 