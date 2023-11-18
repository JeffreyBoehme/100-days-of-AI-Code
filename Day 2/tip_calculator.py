total = input("How much was the total bill?\n")

people = input("How many peeople are splitting the bill?\n")

tip_amount = input("What percentage would you like to tip?\n")

calculated_amount = float(total) / float(people)
calculated_tip = (calculated_amount / 100) * float(tip_amount)
print(f"the per person cost is ${calculated_amount}")
print(f"the per person tip is ${calculated_tip}")

calculated_total = calculated_amount + calculated_tip
print(f"the total is ${calculated_total}")
print(
    f"Which means you should pay ${calculated_amount} for your meal because tipping is stupid."
)
