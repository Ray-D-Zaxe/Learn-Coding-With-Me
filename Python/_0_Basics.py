# This is a comment
# A comment in programming does not get processed
# Its utility/use/purpose is to help the person reading the code

''' Triple quotation
can be used for
multi-line comments'''

""" This is also
considered as triple 
quotation """



a = 10                          # This is a variable (or var)
a = 3                           # Its value can be changed
a = 6.7                         # The same var can hold a different type of value (or val)
a = 7.5                         # This is called a float or floating point val
a = -8                          # And this ofcourse is our classic integer val
a = 8j                          # This is a complex val
a = True                        # This is a bool or boolian val
a = False
a = "Hello World"               # This val is a string
a = 'Hello World'               # This val is also a string



print('Hello World')            # This is the print function
print("What's up ?")            # Its is used to print values
# Use of   ^ (') in the above print was made possible by using ("") to encapsulate the string



print(a)                        # We can directly print our variables
print("a =", a)                 # we could do this but this can get complicated with more variables

print(f"a = {a}")               # this is a formatted print, the values inside {} get evaluated
#     ^ this (f) is used to tell the system that its a formatted print



b = input("Enter a value : ")   # used to take user input
print(f'b = {b}')

b = int(input("Enter an integer value : ")) # by using int(), we tell the system to treat the input as an integer
print(f"b = {b}")               # if input is not an integer, it will result into an error
