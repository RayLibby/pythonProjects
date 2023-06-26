#Write your code below this row 👇

totalSum = 0

for numbers in range(1,101):
    if numbers%2 == 0:
        totalSum += numbers

print(totalSum)

'''
# alternative method

even_sum = 0
for number in range(2, 101, 2):
  # print(number)
  even_sum += number
print(even_sum)
  

'''

