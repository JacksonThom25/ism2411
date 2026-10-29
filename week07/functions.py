# Self-Assessment
# 1. I found the bugs by reading the errors and checking the code.
# Debugging helped me see how small mistakes can affect a program.
#
# 2. apply_discount takes a price and a customer tier, applies the
# correct discount, and returns the discounted price. A colleague
# can use it by providing a price and a tier such as "gold".
#
# # AI Disclosure: I used ChatGPT for help understanding errors
# and checking my code.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

taxed_price = discounted_price + calculate_tax(discounted_price, 0.07)
print(f"After tax: ${taxed_price:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


 # --- Exercise 5: Fixed Broken Sales ---
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100  # global variable

def double_it():
    x = 999  # local variable, different from global x
    return x * 2

print(x)
print(double_it())
print(x)