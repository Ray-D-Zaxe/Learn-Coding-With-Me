# Defining the Functions

global_var = global_var_1 = global_var_2 = global_var_3 = 0


def func():                                     # No Argument
    print("This is a basic function.")
    return



def arg1(arg):                                  # 1 Argument
    print(f"This is a function with one argument, argument : {arg}")
    return None



def sum(a, b):                                  # Multi-Argument with return
    return a + b



def  intro(name, age):                          # Multi-Argument
    print(f"Name : {name}\nAge : {age}")



def greet(name = "stranger"):                   # Default Argument
    print(f"Hello, {name}")



def sum_All(*args):                             # Variable Length Arguments using Tupils
    result = 0
    for num in args:
        result += num
    return result



def display_Info(**kwargs):                     # Variable Length Arguments using Dictonary
    for key, value in kwargs.items():
        print(f"{key} : {value}")



def var(g1, g3):                                # Scope Detection
    local_var = 10
    global global_var_2
    
    print(f"(inside var function) [before change] global_var : {global_var}")
    print(f"(inside var function) [before change] g1 (global_variable_1) : {g1}")
    print(f"(inside var function) [before change] global_var_2 : {global_var_2}")
    print(f"(inside var function) [before change] g3 (global_variable_3) : {g3}")
    print(f"(inside var function) [before change] local_var : {local_var}")

    #global_var += 1                            error cuz global_var does't exist and isn't defined in any
                                                # capacity inside the var function
    g1 += 1
    global_var_2 += 1
    g3 += 1
    local_var += 1
    
    print(f"(inside var function) [before change] global_var : {global_var}")
    print(f"(inside var function) [after change] g1 (global_variable_1) : {g1}")
    print(f"(inside var function) [after change] global_var_2 : {global_var_2}")
    print(f"(inside var function) [before change] g3 (global_variable_3) : {g3}")
    print(f"(inside var function) [after change] local_var : {local_var}")
    return g3



def chng_lst(lst):                              # Call by Reference or Pass by Object Reference
    lst[0] = 47



def fact(i):                                    # Recursive Function
    if i > 1:
        return (fact(i - 1) * i)
    else:
        return 1



sqr = lambda x : x * x                          # Lambda Function, takes x as argument, one-liner


# -----------------------------------------------------------------------------------------------------------
# Calling the Functions
# -----------------------------------------------------------------------------------------------------------

func                                            # doesn't do anything, cuz it calls the object not the function
basic_f = func                                  # passes func as an object to variable basic_f
basic_f                                         # doesn't do anything, cuz it calls the object not the function
print(f"func : {func}")                         # WORKS!!!, i.e, prints the location of function func
print(f"basic_f : {basic_f}")                   # WORKS!!!, i.e, prints the location of function func
print(f"basic_f() : {basic_f()}")               # WORKS!!!, i.e, calls the function
print(f"func() : {func()}")                     # WORKS!!!, i.e, calls the function
print()



arg1                                            # doesn't do anything, cuz it calls the object not the function
argument_func = arg1                            # passes func as an object to variable basic_f
argument_func                                   # doesn't do anything, cuz it calls the object not the function
#argument_func()                                error, cuz this func needs atleast 1 argument
argument_func("Yohohoho")                       # WORKS!!!, i.e, calls the function
argument_func = arg1("Brook")                   
argument_func                                   # WORKS!!!, i.e, calls the function
#argument_func()                                error, cuz this func needs atleast 1 argument                         
print(f"argument_func : {argument_func}")       # returns None
#print(f"argument_func() : {argument_func()}")  error, cuz this func needs atleast 1 argument
print(f'arg1("21 Pilots") : {arg1("21 Pilots")}')
                                                # WORKS!!!, i.e, calls the arg1 function then the print function
print()



print(f"sum(2, 3) : {sum(2, 3)}")               # WORKS!!!, i.e, calls the function
suum = sum(4, 5)
#print(f"suum = sum(4, 5), suum() : {suum()}")  error cuz object suum() not callable
print(f"suum = sum(4, 5), suum : {suum}")       # WORKS!!!, i.e, calls the function
print()



print(f'intro(age = 21, name = "Erroneous") : {intro(age = 21, name = "Erroneous")}')
                                                # WORKS!!!, i.e, calls the function
print()



print(f"greet : {greet}")                       # WORKS!!!, i.e, prints the location of function greet
print(f"greet() : {greet()}")                   # WORKS!!!, i.e, calls the function
print(f'greet("Erroneous") : {greet("Erroneous")}')
                                                # WORKS!!!, i.e, calls the function
print()



print(f"sum_All(4, 6, 7, 8, 9, 0, 3) = {sum_All(4, 6, 7, 8, 9, 0, 3)}")
                                                # WORKS!!!, i.e, calls the function
print()



function_list = [sum, intro]                    # creats a list of functions
print(f"function_list[0] : {function_list[0]}") # WORKS!!!, i.e, prints the location of function sum
print(f"function_list[1] : {function_list[1]}") # WORKS!!!, i.e, prints the location of function intro
print(f"function_list[0](3, 4) : {function_list[0](3, 4)}")
                                                # WORKS!!!, i.e, calls the sum function and then the print
                                                # function
print(f"function_list[1]('Namaewa', 21) : {function_list[1]('Namaewa', 21)}")
                                                # WORKS!!!, i.e, calls the intro function and then the print
                                                # function
print()



#display_Info('c', 8, "yoo, 7.9")               error cuz no variable name, i.e, 'key' was provided
display_Info(character_value = 'c', integer_value = 8, string_value = "yoo", float_value = 7.9)
                                                # WORKS!!!, i.e, calls the display_Info function
print("\n\n")



var(global_var_2, global_var_3)                 # WORKS!!!, i.e, calls the function
print(f"(outside var function) global_var : {global_var}")
                                                # Value could't be accessed inside the var function
print(f"(outside var function) g1 (global_variable_1) : {global_var_1}")
                                                # Value passed as an argument but didn't change
print(f"(outside var function) global_var_2 : {global_var_2}")
                                                # Value passed through global keyword did change
print(f"(outside var function) g3 (global_variable_3) : {global_var_3}")
                                                # Value passed as an argument and returned as the same argument
                                                # but didn't change
#print(f"(inside var function) local_var : {local_var}")
                                                # error cuz local_var does't exist and isn't defined in any
                                                # capacity outside the var function
print()



lst = [9, 8, 7, 6]
print(f"list [before change function] : {lst}")
chng_lst(lst)                                  # WORKS!!!, i.e, calls the function and changes the value
print(f"list [after change function] : {lst}")
print()



print(f"fact(5) : {fact(5)}")                   # WORKS!!!, i.e, calls the function
print()



print(f"sqr(5) : {sqr(5)}")                     # WORKS!!!, i.e, calls the function
print()



# Some other Lambda examples

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)                                  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)                             # Output: [2, 4, 6, 8, 10]
print()