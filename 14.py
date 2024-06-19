# Program to print multiple input lines of text after the user presses enter on an empty line.
def main(): 
    lines = [] 
    print("Enter multiple lines of text. Press Enter on an empty line to stop.") 
    while True: 
        line = input() 
        if line == "": 
            break 
        lines.append(line) 
    if lines: 
        print("\nAll lines entered:") 
        for line in lines: 
            print(line) 
    else: 
        print("No lines entered.") 
if __name__ == "__main__": 
    main() 