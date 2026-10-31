
# ISM 2411 - Module 10 Lab
# Name: Jackson Thom

# Reflection 1:
# The most surprising thing about Python lists is that you can
# add, remove, and change items without creating a new list.
# I also learned that Python starts counting positions at 0
# instead of 1, which was different from what I expected.

# Reflection 2:
# At my job at Jennie's Pizzeria, we keep track of takeout orders
# and inventory throughout each shift. A Python list could help
# organize orders and calculate totals automatically instead
# of manually entering everything into Excel.


# --- Exercise 1: Build the List ---

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# --- Exercise 2: Index Practice ---

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# --- Exercise 3: Slicing ---

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# --- Exercise 4: Modify ---

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# --- Exercise 5: Tuple Comparison ---

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for coordinates because their values stay the same.")

print(coords)


# --- Exercise 6: Average of a List of Sales ---

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)


# --- Exercise 7: Accumulator Pattern ---

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)


# --- Exercise 8: Filter Above Threshold ---

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_average = sum(high_sales) / high_count

print("High sales:", high_sales)
print("Count:", high_count)
print(f"Average: {high_average:.2f}")
