def my_decorator(func):
    # func()
    # wrapper() it is not defined yet
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper



@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# print(say_whee())
