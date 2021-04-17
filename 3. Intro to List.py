# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:23:56 2021

@author: Sameer Thakare
"""
#----------------------------------------------------------------------------------------------#

"""
What Is a List?
  - A list is a collection of items in a particular order. 
  - You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names. 
  - In Python, square brackets ([]) indicate a list, and individual elements 
    in the list are separated by commas.
"""
#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)

#----------------------------------------------------------------------------------------------#

"""
Accessing Elements in a List
  - Lists are ordered collections, so you can access any element in a list by 
    telling Python the position, or index, of the item desired. 
  - To access an element in a list, write the name of the list followed by the index of the item 
    enclosed in square brackets.
  - Index Positions Start at 0, Not 1
"""

#val = bicycles[3]
#print(val)

# Using string methods with list elements
#print(bicycles[2].title())

# Python has a special syntax for accessing the last element in a list.
#The index -2 returns the second item from the end of the list, 
#the index -3 returns the third item from the end, and so forth.

#print(bicycles[-4])

#----------------------------------------------------------------------------------------------#

# Changing, Adding, and Removing Elements

"""
Modifying Elements in a List
  - The syntax for modifying an element is similar to the syntax for accessing an element in a list. 
  - To change an element, use the name of the list followed by the index of the element you want to change, 
    and then provide the new value you want that item to have.
"""

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[-1] = 'ducati'
#print(motorcycles)

#print(motorcycles)

# List is mutable 
#----------------------------------------------------------------------------------------------#
"""
Adding Elements to a List
  - Python provides several ways to add new data to existing lists.
  - The simplest way to add a new element to a list is to append the item to the list.
  - You can add a new element at any position in your list by using the insert() method.
"""

# Using append

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)

# Using insert

#motorcycles = ['honda', 'yamaha', 'suzuki'] 
#motorcycles.insert(0, 'ducati')
#print(motorcycles)

#----------------------------------------------------------------------------------------------#
"""
Removing Elements from a List
  - remove an item or a set of items from a list.
  - If you know the position of the item you want to remove from a list, you can 
    use the del statement. 
  - The pop() method removes the last item in a list, but it lets you work 
    with that item after removing it.
  - You can use pop() to remove an item from any position in a list by including 
    the index of the item.
  - If you only know the value of the item you want to remove, you 
    can use the remove() method.
"""
# Removing an Item Using the del Statement

"""
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

del motorcycles[0] 
print(motorcycles)
"""

# Removing an Item Using the pop() Method
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)
"""

# Popping Items from any Position in a List
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(first_owned)
"""

# Removing an Item by Value
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
"""
#----------------------------------------------------------------------------------------------#
"""
Organizing the list
  - Lists are created in an unpredictable order. 
  - We need to present your information in a particular order. 
  - Requires modification of list or preserving the list. 
  - Python provides a number of different ways to organize your lists.
"""


# Sorting a List Permanently with the sort() Method
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
"""

# To sort list in reverse alphabetical order by passing the argument reverse=True.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
"""
#----------------------------------------------------------------------------------------------#

# Sorting a List Temporarily with the sorted() Function
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
"""

# The sorted() function can also accept a reverse=True argument 
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))
"""
#----------------------------------------------------------------------------------------------#
# Printing a List in Reverse Order
# The reverse() method changes the order of a list permanently
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
"""
#----------------------------------------------------------------------------------------------#

# Finding the Length of a List

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(len(cars))

#----------------------------------------------------------------------------------------------#