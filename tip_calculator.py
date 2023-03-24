print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

pax = input("How many people to split the bill? ")


per_pax = (float(bill) / int(pax)) * ((100 + int(tip))/100)

print(f"Eash person should pay ${round(per_pax,2)}")
