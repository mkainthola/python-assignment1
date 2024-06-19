# Program that takes a list of numbers and returns their sum.
def sum_of_numbers(numbers): 
    total = 0 
    for num in numbers: 
        total += num 
    return total 
def main(): 
    try: 
        input_numbers = input("Enter a list of numbers separated by spaces: ") 
        numbers = list(map(float, input_numbers.split())) 
        total_sum = sum_of_numbers(numbers)
        print(f"\nSum of the numbers: {total_sum}") 
    except ValueError: 
        print("Error: Please enter valid numbers separated by spaces.") 
if __name__ == "__main__": 
    main() 