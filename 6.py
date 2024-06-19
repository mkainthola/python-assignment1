# Program to read content from a text file and print it to the console 
file_name = "doc.txt" 
try: 
    with open(file_name, "r") as file: 
        content = file.read() 
        print("Content of the file:") 
        print(content) 
except FileNotFoundError: 
    print("The file", file_name, "was not found.") 