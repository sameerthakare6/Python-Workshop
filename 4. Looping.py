# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 01:40:04 2021

@author: Sameer Thakare
"""
#----------------------------------------------------------------------------------------------#

# Looping
"""
Looping Through an Entire List
  - loops are use to run through all entries in a list, performing the same 
    task with each item
  - you can use for loop to perform same action with every item in a list.
"""

"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)
"""
#----------------------------------------------------------------------------------------------#

# A Closer Look at Looping
"""
  - Python initially reads the first line of the loop
  - next it retrieve the first value from the list magicians and associate it with the variable magician.
  - Python prints the current value of magician. Because the list contains more values, Python returns 
    to the first line of the loop
  - Python retrieves the next name in the list, and associates that value with the variable magician.
"""
"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)
"""
#----------------------------------------------------------------------------------------------#

# Avoiding Indentation Errors
"""
  - Python uses indentation to determine how a line, or group of lines, is related 
    to the rest of the program.
  - Python’s use of indentation makes code very easy to read. 
  - Basically, it uses whitespace to force you to write neatly formatted code with a clear visual structure.
  - Helps in better organization of project.
  - Always indent the line after the for statement in a loop.
"""
#----------------------------------------------------------------------------------------------#
# Using the colon

"""
  - The colon at the end of a for statement tells Python to interpret the next 
    line as the start of a loop.
  - Dont forget the colon after for statement.
"""
#----------------------------------------------------------------------------------------------#

# Making Numerical Lists

"""
  - Lists are ideal for storing sets of numbers, and Python provides a variety of tools to 
    help you work efficiently with lists of numbers. 
  - 
"""
# Using the range() Function
# Python’s range() function makes it easy to generate a series of numbers. 
"""
for value in range(1, 5):
    print(value)
"""
# Using range() to Make a List of Numbers

"""
numbers = list(range(1, 6))
print(numbers)
"""
# If you pass a third argument to range(), Python uses that value as a step size.
"""
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)
"""
#----------------------------------------------------------------------------------------------#

# Program to generate a list to find square of numbers in range
"""
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)
"""
#----------------------------------------------------------------------------------------------#

# List Comprehensions
# A list comprehension allows you to generate this same list in just one line of code.

"""
squares = [value**2 for value in range(1, 11)]
print(squares)
"""

#----------------------------------------------------------------------------------------------#
# Slicing a List

# To make a slice, you specify the index of the first and last elements you  want to work with.
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[-3:])
"""
#----------------------------------------------------------------------------------------------#

# Copying a List
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
"""
#----------------------------------------------------------------------------------------------#

