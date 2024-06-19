# Program that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(input_string, prefix, suffix): 
    starts_with_prefix = input_string.startswith(prefix) 
    ends_with_suffix = input_string.endswith(suffix) 
    return starts_with_prefix, ends_with_suffix 
def main(): 
    input_string = input("Enter a string: ") 
    prefix = input("Enter the prefix to check (or leave blank if none): ") 
    suffix = input("Enter the suffix to check (or leave blank if none): ") 
    starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix) 
    if prefix and suffix: 
        print(f"\nThe string '{input_string}' starts with '{prefix}'? {starts_with_prefix}") 
        print(f"The string '{input_string}' ends with '{suffix}'? {ends_with_suffix}") 
    elif prefix: 
        print(f"\nThe string '{input_string}' starts with '{prefix}'? {starts_with_prefix}") 
    elif suffix: 
        print(f"\nThe string '{input_string}' ends with '{suffix}'? {ends_with_suffix}") 
    else: 
        print("You didn't enter any prefix or suffix to check.") 
if __name__ == "__main__": 
    main() 