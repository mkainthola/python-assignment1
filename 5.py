# Program to write user input to a text file 
user_input = input("Enter a string: ") 
file_name = "doc.txt" 
with open(file_name, "w") as file: 
    file.write(user_input) 
print("The string has been written to", file_name) 