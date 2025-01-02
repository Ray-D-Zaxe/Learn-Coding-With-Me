# String Operators

str1 = "Hello World, whats up?"

print(str1)
print()



# Slice Operator

str1[0]                     # H
str1[1]                     # e
str1[-1]                    # ?
str1[-2]                    # p



# Range Slice

str1[:]                     # Hello World, whats up?
str1[1:]                    # ello World, whats up?
str1[:3]                    # Hel
str1[:0]                    # Returns nothing, empty string ?
str1[3:7]#lo W

str1[-1:]                   # ?
str1[:-1]                   # Hello World, whats up
str1[2:-2]                  # llo World, whats u
str1[-1:-9]                 # Returns nothing, empty string ?
str1[-9:-1]                 # whats up



str1[0:6] * 5               # Hello Hello Hello Hello Hello
5 * str1[0:6]               # Hello Hello Hello Hello Hello



'Hel' in str1               # True
'Halo' in str1              # False
'Hel' not in str1           # False
'Halo' not in str1          # True



print('C://python37\n')     # C://python37
print(r'C://python37\n')    # C://python37\n
print()



print("1 : %d, '2' : %s, 3.0 : %f" %(1, '2', 3.0))
                            # 1 : 1, '2' : 2, 3.0 : 3.000000
print()



print('''They said, "What's going on?"''')
                            #They said, "What's going on?"
print('They said, "What\'s going on?"')
                            # They said, "What's going on?"
print("They said, \"What's going on?\"")
                            # They said, "What's going on?"
print()



print("P1 \
P2 \
P3")                        # P1 P2 P3
print()



print("\\ \" \a 123\b456")  # \ "  12456
print("12\f34\n56\r78\t90\v-+")
print("777 in Octal ASCII : \777\nFF in Hexa-Decimal ASCII : \xFf")
                            # 777 in Octal ASCII : ǿ
                            # FF in Hexa-Decimal ASCII : ÿ
print()



print("{} and {}".format("A","B"))
                            # A and B
print("{0} and {1}".format("C","D"))
                            # C and D
print("{a}{b}{c}".format(a = "H", c = "O", b = 2))
                            # H2O
print()



# String Method/Functions (NOTE : Doesn't change the orignal, rather creates an edited copy)

str1                        # Hello World, whats up?
str1.capitalize()           # Hello world, whats up?
str1.casefold()             # hello world, whats up?
str1.center(4, '-')         # Hello World, whats up?
str1.islower()              # False
str1.isupper()              # Flase
str1.isspace()              # False
str1.upper()                # HELLO WORLD, WHATS UP?
str1.lower()                # hello world, whats up?
str1.title()                # Hello World, Whats Up?
str1.swapcase()             # hELLO wORLD, WHATS UP?