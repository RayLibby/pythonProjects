# Write your code below this row 👇

for numbers in range(1, 101):
    # divisible by 3 only
    if numbers % 3 == 0 and numbers % 5 != 0:
        print("Fizz")
    # divisible by 5 only
    elif numbers % 5 == 0 and numbers % 3 != 0:
        print("Buzz")
    # divisible by 3 and 5
    elif numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    # rest of numbers
    else:
        print(numbers)

    '''
  # The Class solution:
  
    
    #Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
    
    '''
