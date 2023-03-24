print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

pax = int(input("How many people to split the bill? "))

tip_percent = tip/100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount

per_pax = "{:.2f}".format(round(total_bill / pax,2)) #"{:.2f}".format( formats for two decimal with last as 0, e.x: 35.60

print(f"Eash person should pay ${per_pax}")
