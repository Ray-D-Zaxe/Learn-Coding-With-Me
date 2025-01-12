try:
    print(x)
except:
    print("An exception occurred") 

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong") 

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished") 
