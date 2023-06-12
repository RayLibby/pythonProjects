# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Book Solution

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
"""

#My Code
DivisibleBy4 = year%4
DivisibleBy100 = year%100
DivisibleBy400 = year%400


if DivisibleBy4 == 0:
    IsDivisibleBy4 = True
else :
    IsDivisibleBy4 = False


if DivisibleBy100 == 0:
    IsDivisibleBy100 = True
else :
    IsDivisibleBy100 = False


if DivisibleBy400 == 0:
    IsDivisibleBy400 = True
else :
    IsDivisibleBy400 = False

#If 1st condition is false then immediately exit at the last Else
if IsDivisibleBy4 is True:
    if IsDivisibleBy100 is False:
        print("Leap year.")
    elif IsDivisibleBy400 is False:
        print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



#print(DivisibleBy4)
#print(IsDivisibleBy4)
#
#print(DivisibleBy100)
#print(IsDivisibleBy100)
#
#print(DivisibleBy400)
#print(IsDivisibleBy400)

"""