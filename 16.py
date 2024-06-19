#program that counts the frequency of each character in a string.
def count_characters(input_string): 
    char_frequency = {} 
    for char in input_string: 
        if char in char_frequency: 
            char_frequency[char] += 1 
        else: 
            char_frequency[char] = 1 
    return char_frequency 
def main(): 
    input_string = input("Enter a string: ") 
    frequency_dict = count_characters(input_string) 
    print("\nCharacter frequencies:") 
    for char, count in frequency_dict.items(): 
        print(f"{char}: {count}") 
if __name__ == "__main__": 
    main() 