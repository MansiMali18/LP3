'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: 04
'''


def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Function to get valid integer input from the user
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Taking user input
n = get_int_input("Enter number of items: ")
weights = [get_int_input(f"Weight of item {i + 1}: ") for i in range(n)]
values = [get_int_input(f"Value of item {i + 1}: ") for i in range(n)]
capacity = get_int_input("Enter capacity of the knapsack: ")

# Calculate maximum value for the 0/1 knapsack
max_value = knapsack(weights, values, capacity)
print(f"Maximum value in the knapsack: {max_value}")

'''

OUTPUT:
Enter number of items: 3
Weight of item 1: 10
Weight of item 2: 20
Weight of item 3: 30
Value of item 1: 60
Value of item 2: 100
Value of item 3: 120
Enter capacity of the knapsack: 50
Maximum value in the knapsack: 220

'''