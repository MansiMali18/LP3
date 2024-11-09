#Name : Mansi Mali
#Roll No. 41
#Sub : DAA
#Experiment No : 3
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost = value / weight  # Cost per unit weight

def fractional_knapsack(capacity, items):
    # Sort items by cost per unit weight in descending order
    items.sort(key=lambda item: item.cost, reverse=True)

    total_value = 0.0  # Total value accumulated
    for item in items:
        if capacity >= item.weight:
            # If the knapsack can carry the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # If the knapsack can't carry the whole item, take the fractional part
            total_value += item.cost * capacity
            break  # Knapsack is full

    return total_value

# User input
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        value = float(input(f"Enter the value of item {i + 1}: "))
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)

    print(f"The maximum value in the knapsack is: {max_value:.2f}")
