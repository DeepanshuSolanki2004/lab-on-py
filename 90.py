# WAP in python to demonstrate class, objects, properties and methods

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Example usage
car1 = Car("Suzuki", "Grand Vitara", 2024)
car1.display_info()
print("THIS CODE IS WRITTEN BY DEEPANSHU SOLANKIA ERP- 0221BCA005")
