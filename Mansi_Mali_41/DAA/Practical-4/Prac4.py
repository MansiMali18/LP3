#Name : Mansi Mali
#Roll No. 41
#Sub : DAA
#Experiment No : 4
def knapsack(weights, values, capacity):
    n = len(values)
    # Create a 2D array to store maximum values
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The maximum value for the full capacity

# User input
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    values = []
    weights = []

    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)

    capacity = int(input("Enter the capacity of the knapsack: "))
    max_value = knapsack(weights, values, capacity)

    print(f"The maximum value in the knapsack is: {max_value}")
