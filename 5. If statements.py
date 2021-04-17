# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 03:08:15 2021

@author: Sameer Thakare
"""
#----------------------------------------------------------------------------------------------#
# Simple if Statements
"""
    if conditional_test:
       do something
"""
# simple example
# Indentation plays the same role in if statements as it did in for loops.

"""
age = 19
if age >= 18:
    print("You are old enough to vote!")
"""
#----------------------------------------------------------------------------------------------#

# if-else Statements

"""
  - An if-else block is similar to a simple if statement
  - else statement allows you to define an action or set of actions that are executed when the 
    conditional test fails.
"""
# program
"""
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
"""
#----------------------------------------------------------------------------------------------#

# The if-elif-else Chain

"""
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $25.")
"""
#----------------------------------------------------------------------------------------------#

# Using Multiple elif blocks

"""
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"Your admission cost is ${price}.")
"""
#----------------------------------------------------------------------------------------------#


# Checking Whether a Value Is in a List
"""
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
"""

# Checking Whether a Value Is Not in a List

"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
"""
#----------------------------------------------------------------------------------------------#

