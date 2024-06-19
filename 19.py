# Program that removes all punctuation from a given string.
import string 
def remove_punctuation(input_string): 
    translator = str.maketrans('', '', string.punctuation) 
    return input_string.translate(translator) 
def main(): 
    input_string = input("Enter a string with punctuation: ") 
    cleaned_string = remove_punctuation(input_string) 
    print("\nString without punctuation:") 
    print(cleaned_string) 
if __name__ == "__main__": 
    main() 