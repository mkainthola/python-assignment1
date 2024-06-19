# Program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def celsius_to_fahrenheit(celsius): 
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 
def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5/9 
    return celsius 
def main(): 
    try: 
        choice = input("Choose conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your choice (1 or 2): ") 
        if choice == '1': 
            celsius = float(input("Enter temperature in Celsius: ")) 
            fahrenheit = celsius_to_fahrenheit(celsius) 
            print(f"{celsius} degrees Celsius = {fahrenheit:.2f} degrees Fahrenheit") 
        elif choice == '2': 
            fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 
            celsius = fahrenheit_to_celsius(fahrenheit) 
            print(f"{fahrenheit} degrees Fahrenheit = {celsius:.2f} degrees Celsius") 
        else: 
            print("Invalid choice. Please enter either 1 or 2.") 
    except ValueError: 
        print("Invalid input. Please enter a valid number for temperature.") 
if __name__ == "__main__": 
    main() 