# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}.")

""" 
#My Solution

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25 


if add_pepperoni == "Y":
    if size == "S":
        total += 2
    if size =="M" or size =="L":
        total += 3    
else: total += 0


if extra_cheese == "Y":
    total += 1
else: total +=0

print(f"Your final bill is: ${total}.")
"""