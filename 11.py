# Program to generate the first n numbers in the Fibonacci sequence 
def fibonacci_sequence(n): 
    fib_sequence = [0, 1] 
    for i in range(2, n): 
        next_num = fib_sequence[-1] + fib_sequence[-2] 
        fib_sequence.append(next_num) 
    return fib_sequence[:n] 
n = int(input("Enter the number of Fibonacci numbers to generate: ")) 
fib_numbers = fibonacci_sequence(n) 
print("The first", n, "numbers in the Fibonacci sequence are:") 
print(fib_numbers) 