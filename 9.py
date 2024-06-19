# Program to check if a substring is present in a given string 
main_string = input("Enter the main string: ") 
substring = input("Enter the substring to check: ") 
if substring in main_string: 
    print("The substring '{0}' is present in the main string.".format(substring)) 
else: 
    print("The substring '{0}' is not present in the main string.".format(substring)) 