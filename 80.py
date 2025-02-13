#Wap in py to demonstrate decorators with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Jagrit")
print("THIS CODE IS WRITTEN BY DEEPANSHU SOLANKIA ERP- 0221BCA005")