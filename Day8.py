
'''
def first_function():
    answer = input("How do you feel?")
    print(f'I am felling {answer}')
    print('That sounds about right')
    
first_function()    


def greet_with(name,location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

greet_with('Waldo','Florida')    



def greet_with2(name,location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

greet_with2(location = 'Florida',name='Waldo')    
'''
# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  cans = math.ceil((test_h*test_w)/cover)
  print(f"You'll need {cans} cans of paint.")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
