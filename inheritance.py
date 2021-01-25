class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("Vehicle's mileage is ", self.mileage)
        print("Vehicle's cost is ", self.cost)
        print("I am Vehicle")


class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")


c1 = Car(250, 200000)
c1.show_details()
c1.show_car_details()
