'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: 03
'''


def fractional_knapsack(values, weights, capacity):
    # Calculate value to weight ratio and store it with corresponding values and weights
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0

    for value, weight in items:
        if capacity == 0:
            break
        
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0
            
    return total_value

# Taking user input
n = int(input("Enter number of items: "))
values = [int(input(f"Value of item {i + 1}: ")) for i in range(n)]
weights = [int(input(f"Weight of item {i + 1}: ")) for i in range(n)]
capacity = int(input("Enter capacity of the knapsack: "))

# Calculate maximum value for the fractional knapsack
max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in the knapsack: {max_value:.2f}")

'''

OUTPUT:
Value of item 1: 60
Value of item 2: 100
Value of item 3: 120
Weight of item 1: 10
Weight of item 2: 20
Weight of item 3: 30
Enter capacity of the knapsack: 50
Maximum value in the knapsack: 240.00

'''