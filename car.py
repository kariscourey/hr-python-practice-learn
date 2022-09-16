class Car:

    # This is NOT a variable
    # This is a static attribute (property) of the class
    num_doors = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        # print(num_doors)
        print(self.num_doors)
        print("Beep beep")


car = Car("Toyota", "Sienna", 2015)

print(car.make)
print(car.num_doors)


class Car(models.Model):
    make = models.CharField(max_length=100)
    num_doors = 4  # not a field in db


class User(models.Model):
    first_name: models.CharField()
    last_name: models.CharField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

def user_detail(request)
    user = User.objects.filter()
    user.full_name()

    context = {
        "full_name": full_name,
    }

    return render(request, "template.html", context)

print(car.make)
