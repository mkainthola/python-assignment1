#Program to calculate the factorial of a number.
def factorial_iterative(n): 
    result = 1 
    for i in range(1, n + 1): 
        result *= i 
    return result 
number = int(input("Enter a number: ")) 
factorial = factorial_iterative(number) 
print("The factorial of {0} is {1}".format(number, factorial)) 