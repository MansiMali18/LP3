#Name : Mansi Mali
#Roll No. 41
#Sub : DAA
#Experiment No : 1
import time

# Non-recursive approach (Iterative)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

# Recursive approach
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Time complexity analysis
def analyze_fibonacci(n):
    # Iterative Fibonacci
    start_time = time.time()
    iterative_result = fibonacci_iterative(n)
    iterative_time = time.time() - start_time

    # Recursive Fibonacci
    start_time = time.time()
    recursive_result = fibonacci_recursive(n)
    recursive_time = time.time() - start_time

    print(f"Iterative Fibonacci({n}): {iterative_result} (Time: {iterative_time:.6f} seconds)")
    print(f"Recursive Fibonacci({n}): {recursive_result} (Time: {recursive_time:.6f} seconds)")

    # Complexity Analysis
    print("\nTime and Space Complexity Analysis:")
    print("1. Iterative (Non-recursive) Fibonacci:")
    print("   Time Complexity: O(n) - We iterate through n steps to compute the result.")
    print("   Space Complexity: O(1) - Only a constant amount of extra space is used.")
    
    print("2. Recursive Fibonacci:")
    print("   Time Complexity: O(2^n) - Each call generates two more recursive calls, leading to exponential growth.")
    print("   Space Complexity: O(n) - The recursive call stack grows linearly with n.")

    print("\nConclusion:")
    print("The iterative solution is far more efficient than the recursive solution in both time and space.")
    print("The recursive approach is much slower because of repeated calculations and has a higher space complexity due to the call stack.")

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer to compute Fibonacci: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            analyze_fibonacci(n)
    except ValueError:
        print("Invalid input! Please enter an integer.")
