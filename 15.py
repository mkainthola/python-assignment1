# Program that reads data from a CSV file and prints it to the console.
import csv 
def main(): 
    csv_file = 'data.csv'      
    try: 
        with open(csv_file, mode='r', newline='') as file: 
            reader = csv.reader(file) 
            print("Contents of the CSV file:") 
            for row in reader: 
                print(', '.join(row))  # Join elements of row with ', ' for better formatting 
    except FileNotFoundError: 
        print(f"Error: The file '{csv_file}' was not found.") 
    except IOError as e: 
        print(f"Error: {e}") 
if __name__ == "__main__": 

    main() 