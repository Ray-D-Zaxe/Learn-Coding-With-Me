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
a = "Hello World"               # This val is a string
a = 'Hello World'               # This val is also a string
a = True                        # This is a bool or boolian val
a = False
a = 7.5                         # This is called a float or floating point val
a = -8                          # And this ofcourse o+is our classic integer val


print('Hello World')            # This is the print function
print("What's up ?")            # Its is used to print values
# Use of   ^ (') in the above print was made possible by using ("") to encapsulate the string


print(a)                        # We can directly print our variables
print("a =", a)                 # we could do this but this can get complicated with more variables

print(f"a = {a}")               # this is a formatted print, the values inside {} get evaluated
#     ^ this (f) is used to tell the system that its a formatted print
print(f"a + 10 = {a + 10}")



b = input("Enter a value : ")   # used to take user input
print(f'b = {b}')

b = int(input("Enter an integer value : ")) # by using int(), we tell the system to treat the input as an integer
print(f"b = {b}")               # if input is not an integer, it will result into an error



a = b = 5                       # both a and b will have the value 5
a, b = 5, "Hi"                  # a = 5, and, b = "Hi"
