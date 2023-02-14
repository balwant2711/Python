print("Welcome to tip calculator!")
bill = float(input("What was the total bill ? $\n"))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15\n"))
people = int(input("How many people to split the bill ?\n"))

bill_with_tip = tip/100 * bill + bill 
#OR

# bill_with_tip = bill * (1 + tip / 100)
#OR

# tip_as_percentage = tip / 100
# total_tip_amount = bill * tip_as_percentage
# total_bill = bill + total_tip_amount



# print(bill_with_tip)

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount ="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

