# Program that copies the contents of one text file to another.
def copy_file(source_file, destination_file): 
    try: 
        with open(source_file, 'r') as src: 
            with open(destination_file, 'w') as dest: 
                dest.write(src.read()) 
        print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.") 
    except FileNotFoundError: 
        print(f"Error: File '{source_file}' not found.") 
    except Exception as e: 
        print(f"Error: {e}") 
def main(): 
    try: 
        source_file = input("Enter the path to the source text file: ").strip() 
        destination_file = input("Enter the path to the destination text file: ").strip() 
        copy_file(source_file, destination_file) 
    except Exception as e: 
        print(f"Error: {e}") 
if __name__ == "__main__": 
    main()