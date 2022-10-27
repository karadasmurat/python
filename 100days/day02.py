print("Welcome to the bill share.")
bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person = bill * (1 + (tip_percentage / 100)) / number_of_people
print(f"Each person should pay: {round(bill_per_person, 2)}")