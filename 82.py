#WAP in py to demonstare how decorators work

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("THIS CODE IS WRITTEN BY DEEPANSHU SOLANKIA ERP- 0221BCA005")
