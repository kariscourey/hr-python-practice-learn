class Car:

    # This is NOT a variable
    # This is a static attribute of the class
    num_doors = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("Toyota", "Sienna", 2015)

print(car.make)
print(car.num_doors)
