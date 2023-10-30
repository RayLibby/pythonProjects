# Write your code below this line 👇
def prime_checker(number):
  if n < 101:
    test1 = n%n
    test2 = n%1
    if test1 + test2 > 0:
        print('This is a prime number')
    else:
        print('The is not a prime number')    
  else:
    print('select a number been 1 and 100')




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)