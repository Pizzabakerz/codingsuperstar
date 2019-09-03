print("line before error")

# f = open('jack.mov', 'r') # this is the error

# line after error
try:
    a = input("username: ")
    b = input("password: ")

    if a=="jack" and b =="1234":
        print("you are allowed to view this")
    else:
        raise PermissionError

except PermissionError as e:
    print("you are not allowed")

except FileNotFoundError as e:
    print("sorry your file was not found")

except ValueError as e:
    print("please enter a valid number")

except ZeroDivisionError as e:
    print(e)
    print("anything divided by zero is inifinite")

except Exception as e:
    print(e)
finally:
    print(" i will be out what ever happens")

print("line after error")