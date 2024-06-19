# Program to calculate age when the user inputs birth year.
import datetime 
def calculate_age(birth_year): 
    current_year = datetime.datetime.now().year 
    age = current_year - birth_year 
    return age 
def main(): 
    try: 
        birth_year = int(input("Enter your birth year: ")) 
        age = calculate_age(birth_year) 
        if age >= 0: 
            print(f"You are {age} years old.") 
        else: 
            print("Invalid birth year entered. Please enter a valid year.") 
    except ValueError: 
        print("Invalid input. Please enter a valid year (e.g., 1990).") 
if __name__ == "__main__": 
    main() 