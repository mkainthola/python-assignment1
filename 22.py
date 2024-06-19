# Program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers): 
    if not numbers: 
        return None, None  
    min_value = numbers[0] 
    max_value = numbers[0] 
    for num in numbers: 
        if num < min_value: 
            min_value = num 
        if num > max_value: 
            max_value = num 
    return min_value, max_value 
def main(): 
    try: 
        input_list = input("Enter a list of numbers separated by spaces: ").split() 
        numbers = list(map(float, input_list)) 
        min_value, max_value = find_min_max(numbers) 
        print("\nMinimum value:", min_value) 
        print("Maximum value:", max_value) 
    except ValueError: 
        print("Error: Please enter valid numbers separated by spaces.") 
if __name__ == "__main__": 
    main() 