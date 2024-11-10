'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: 01
'''

import time
import tracemalloc

# Non-Recursive Fibonacci
def fibonacci_non_recursive(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to print the Recursive Fibonacci series
def print_fibonacci_recursive(n):
    series = [fibonacci_recursive(i) for i in range(n)]
    return series

# Function to estimate time complexity
def measure_time_complexity(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

# Function to estimate space complexity
def measure_space_complexity(func, n):
    tracemalloc.start()
    func(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak  # Return peak memory usage in bytes

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))

    # Non-Recursive Fibonacci
    non_recursive_series, non_recursive_time = measure_time_complexity(fibonacci_non_recursive, n)
    non_recursive_space = measure_space_complexity(fibonacci_non_recursive, n)

    print(f"Non-Recursive Fibonacci Series: {non_recursive_series}")
    print(f"Non-Recursive Fibonacci Time taken: {non_recursive_time:.6f} seconds")
    print(f"Non-Recursive Fibonacci Space used: {non_recursive_space / 1024:.2f} KB")
    print("Non-Recursive Fibonacci Theoretical Time Complexity: O(n)")
    print("Non-Recursive Fibonacci Theoretical Space Complexity: O(1)\n")

    # Recursive Fibonacci
    recursive_series, recursive_time = measure_time_complexity(print_fibonacci_recursive, n)
    recursive_space = measure_space_complexity(print_fibonacci_recursive, n)

    print(f"Recursive Fibonacci Series: {recursive_series}")
    print(f"Recursive Fibonacci Time taken: {recursive_time:.6f} seconds")
    print(f"Recursive Fibonacci Space used: {recursive_space / 1024:.2f} KB")
    print("Recursive Fibonacci Theoretical Time Complexity: O(2^n)")
    print("Recursive Fibonacci Theoretical Space Complexity: O(n)\n")


'''
OUTPUT:
Enter the number of terms: 10
Non-Recursive Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Non-Recursive Fibonacci Time taken: 0.000000 seconds
Non-Recursive Fibonacci Space used: 0.16 KB
Non-Recursive Fibonacci Theoretical Time Complexity: O(n)        
Non-Recursive Fibonacci Theoretical Space Complexity: O(1)       

Recursive Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]    
Recursive Fibonacci Time taken: 0.000000 seconds
Recursive Fibonacci Space used: 0.16 KB
Recursive Fibonacci Theoretical Time Complexity: O(2^n)
Recursive Fibonacci Theoretical Space Complexity: O(n)
'''