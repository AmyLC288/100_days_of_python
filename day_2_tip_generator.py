#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to our Handy Tip Calculator.\n")
total_bill = input("What was the total bill? \n$")
tip = int(input("What percentage tip would you like to leave? 10, 12 or 15?\n"))
split_bill = int(input("How many people to split the bill?\n"))

percentage_tip = 1 + tip / 100
total_with_tip = float(total_bill) * percentage_tip
total_per_person = float(total_with_tip) / split_bill
total_per_person =  round(total_per_person, 2)

print(f"Each person should pay: ${total_per_person}")