# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = (name1 + name2).lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l = names.count("l")
o = names.count("o")
v = names.count("v")
e2 = names.count("e")

trueScore = t+r+u+e
loveScore = l+o+v+e2

trueLoveScore = int(str(trueScore) + str(loveScore))

if (trueLoveScore <10) or (trueLoveScore >90):
    print(f"Your score is {trueLoveScore}, you go together like coke and mentos.")
elif (trueLoveScore >= 40) and (trueLoveScore <=50):
    print(f"Your score is {trueLoveScore}, you are alright together.")
else:
    print(f"Your score is {trueLoveScore}.")

#print(type(trueLoveScore))
#print(trueLoveScore)



