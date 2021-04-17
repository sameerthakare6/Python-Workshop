
# First Program : Running hello world program

#print("Sameer")

#----------------------------------------------------------------------------------------------#

"""
COMMENTS
  - In Python, the hash mark (#) indicates a comment.
  - Triple quotes denotes multiline comment
"""
# This is single line comment

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

#----------------------------------------------------------------------------------------------#

# A variable is a container for a value, which can be of various types

"""
VARIABLE RULES
  - Every variable is connected to a value, which is the information associated with
    that variable.
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
  - Spaces are not allowed in variable names
  - Variable names should be short but descriptive.
"""
#VAL = 15
#print(VAL 1)

#----------------------------------------------------------------------------------------------#

"""
STRINGS
  - It is a first data type.
  - A string is a series of characters.
  - You can use single or double quotes around your strings
  - This flexibility allows you to use quotes and apostrophes within your strings:
"""
#print("This is a string.")
#print('This is also a string.')


#print('I told my friend, "Python is my favorite language!"')
#print("The language 'Python' is named after Monty Python, not the snake.")
#print("One of Python's strengths is its diverse and supportive community.")

#----------------------------------------------------------------------------------------------#

# Changing case in string using methods

"""
METHOD
  - A method is an action that Python can perform on a piece of data. 
  - The dot (.) after tells Python to make the title() method act on the variable
  - It follows by parenthesis to provide additional parameters
"""
#name = "ada lovelace"
#print(name.title())


# Changing a string to all uppercase or all lowercase
"""
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
"""
#----------------------------------------------------------------------------------------------#

# Using Variables in Strings

"""
  - To insert a variable’s value into a string, place the letter f immediately 
    before the opening quotation mark. 
  - Put braces around the names of any variable to use inside the string. 
  - Python will replace each variable with its value when the string is displayed.
  - These strings are called f-strings.
"""

"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


message = f"Hello, {full_name.title()}!"
print(message)

full_name = "{} {}".format(first_name, last_name)
print(full_name)
"""

#----------------------------------------------------------------------------------------------#

#arr = [1, 2, 4, 6]
#print(arr[3])


#Adding Whitespace to Strings with Tabs or Newlines

"""
  - Whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. 
  - You can use whitespace to organize your output so it’s easier for users to read.
  - \t is used for tab
  - \n is used for newline
"""
#print("Python")
#print("\tPython")

#print("Languages:\nPython\nC\nJavaScript")

#print("Languages:\n\tPython\n\tC\n\tJavaScript")

#----------------------------------------------------------------------------------------------#

# Stripping Whitespace

# from right side

"""
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
"""

# from left side

"""
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())
"""

# from both the sides


favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())

#----------------------------------------------------------------------------------------------#



