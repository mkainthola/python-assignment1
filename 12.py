# Program to calculate the sum of digits of a given number 
def sum_of_digits(number): 
    total_sum = 0 
    while number > 0: 
        total_sum += number % 10 
        number //= 10 
    return total_sum 
number = int(input("Enter a number: ")) 
digit_sum = sum_of_digits(number) 
print("The sum of digits of", number, "is:", digit_sum) 