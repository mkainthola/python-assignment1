# Program that counts the occurrences of a specific element in a list.
def count_occurrences(input_list, element): 
    count = 0 
    for item in input_list: 
        if item == element: 
            count += 1 
    return count 
def main(): 
    try: 
        input_list = input("Enter a list of elements separated by spaces: ").split() 
        element = input("Enter the element to count: ") 
        occurrences = count_occurrences(input_list, element) 
        print(f"\nNumber of occurrences of '{element}' in the list: {occurrences}") 
    except ValueError: 
        print("Error: Please enter valid elements separated by spaces.") 
if __name__ == "__main__": 
    main() 