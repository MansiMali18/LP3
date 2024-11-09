#Name : Mansi Mali
#Roll No. 41
#Sub : DAA
#Experiment No : 5
import time
import threading

# Standard Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Multithreaded Merge Sort Implementation
def merge_sort_threaded(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Creating threads for parallel sorting
        left_thread = threading.Thread(target=merge_sort_threaded, args=(left_half,))
        right_thread = threading.Thread(target=merge_sort_threaded, args=(right_half,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to take input from user and run both sorting algorithms
def run_sorting_with_input():
    # Input from user
    user_input = input("Enter numbers to sort, separated by spaces: ")
    arr = list(map(int, user_input.split()))

    # Copy array for fair comparison
    arr1 = arr[:]
    arr2 = arr[:]

    print("\nStarting sorting...\n")

    # Timing standard merge sort
    start_time = time.time()
    merge_sort(arr1)
    end_time = time.time()
    print(f"Sorted Array (Standard Merge Sort): {arr1}")
    print(f"Time taken by standard merge sort: {end_time - start_time:.6f} seconds")

    # Timing multithreaded merge sort
    start_time = time.time()
    merge_sort_threaded(arr2)
    end_time = time.time()
    print(f"Sorted Array (Multithreaded Merge Sort): {arr2}")
    print(f"Time taken by multithreaded merge sort: {end_time - start_time:.6f} seconds")

# Run the program with user input
run_sorting_with_input()
