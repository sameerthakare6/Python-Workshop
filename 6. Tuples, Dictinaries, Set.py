# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:50:36 2021

@author: Sameer Thakare
"""

"""
TUPLES
  - Tuple is built-in immutable data structure
  - A tuple looks just like a list except you use parentheses instead of square brackets.
"""
# defining the tuple and accessing values
"""
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
"""
# Lets see what happens when we try to change value
# dimensions[0] = 250

#If you want to define a tuple with one element, you need to include a trailing comma:
    
#my_t = (3,)
#print(my_t)

# Looping Through All Values in a Tuple

"""
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
"""
#----------------------------------------------------------------------------------------------#
"""
SET
  - A set is a collection in which each item must be unique
  - Curly braces {} are used to define set
  - To start an empty set use set(), not {} as it denotes empty dictionary
"""

'''
var = {1,3,4,5,2,6,3,4,5,6}
print(var)

#empty set
var = set()
print(var)

# Converting list to set
list_1 = [2,4,5,2,1]
set_1 = set(list_1)
print(set_1)
'''

#----------------------------------------------------------------------------------------------#

"""
Dictionary
  - A dictionary in Python is a collection of key-value pairs
  - Each key is connected to a value, and you can use a key to access the value associated with that key. 
  - A key’s value can be a number, a string, a list, or even another dictionary. 
  - It is wrapped in braces, {}, with a series of key:value pairs inside the braces
"""

alien_0 = {'color': 'green', 'points': 5}
#----------------------------------------------------------------------------------------------#

#Accessing Values in a Dictionary

'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
'''

'''
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
'''
#----------------------------------------------------------------------------------------------#

#Adding New Key-Value Pairs

'''
  - To add a new key-value pair, you would give the name of the dictionary followed by the new key in square 
    brackets along with the new value.
'''

'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
'''
#----------------------------------------------------------------------------------------------#

# Starting with an Empty Dictionary

'''
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
'''
#----------------------------------------------------------------------------------------------#

# Modifying Values in a Dictionary

'''
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
'''
#----------------------------------------------------------------------------------------------#

#Example

'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
 
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
'''

# Now modify alien_0['speed'] = 'fast' and see what happens
#----------------------------------------------------------------------------------------------#

# Removing Key-Value Pairs
'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
'''
#----------------------------------------------------------------------------------------------#

# Using get() to Access Values

'''
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
'''

'''
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
'''

# If you leave out the second argument in the call to get() and the key doesn’t exist, 
# Python will return the value None. The special value None means “no value exists.”
#----------------------------------------------------------------------------------------------#

# Looping Through a Dictionary

# 1. Looping Through All Key-Value Pairs
'''
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
 }

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
'''
#----------------------------------------------------------------------------------------------#

# Example
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
'''
#----------------------------------------------------------------------------------------------#

# Looping Through All the Keys in a Dictionary

# The keys() method is useful when you don’t need to work with all of the values in a dictionary.

'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

for name in favorite_languages.keys():
    print(name.title())
'''

# Check what happens when we only use, for name in favorite_languages:
#----------------------------------------------------------------------------------------------#

# Looping Through a Dictionary’s Keys in a Particular Order
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for the support.")
'''
#----------------------------------------------------------------------------------------------#

# Looping Through All Values in a Dictionary
# Use values() method to return a list of values without any keys.

'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())
'''

#----------------------------------------------------------------------------------------------#

# Nesting

# 1. A List of Dictionaries

'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''

# print(f"\n{aliens[0]}")
#----------------------------------------------------------------------------------------------#
# 2. A List in a Dictionary

'''
# Store information about a pizza being ordered.
pizza = {
     'crust': 'thick',
     'toppings': ['mushrooms', 'extra cheese'],
 }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    #print(f"\t{topping}")
'''

#----------------------------------------------------------------------------------------------#

# 3. A Dictionary in a Dictionary

'''
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
'''
#----------------------------------------------------------------------------------------------#