# program that converts a string into a list of its characters.
def string_to_char_list(input_string): 
    return list(input_string)  

def main(): 
    input_string = input("Enter a string: ") 
    char_list = string_to_char_list(input_string) 
    print(f"List of characters: {char_list}") 
if __name__ == "__main__": 
    main() 