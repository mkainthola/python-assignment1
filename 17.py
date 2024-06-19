# program in python that converts a given string to title case (first letter of each word capitalized).
def convert_to_title_case(input_string): 
    words = input_string.split() 
    title_case_words = [] 
    for word in words: 
        title_case_words.append(word.capitalize()) 
    title_case_string = ' '.join(title_case_words) 
    return title_case_string 
def main(): 
    input_string = input("Enter a string: ") 
    title_case_string = convert_to_title_case(input_string) 
    print(f"\nTitle case string: {title_case_string}") 
if __name__ == "__main__": 
    main() 