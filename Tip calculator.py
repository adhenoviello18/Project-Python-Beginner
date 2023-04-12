#if the bill was £150.00, split between 5 people with 12% tip
#each person should pay (150.00 / 5) * 1.12 = 33.6
#round up to 2 d.p.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")