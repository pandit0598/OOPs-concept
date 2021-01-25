class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("Vehicle's mileage is ", self.mileage)
        print("Vehicle's cost is ", self.cost)
        print("I am Vehicle")


class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("NO. of tyres in the car ", self.tyres)
        print("Horse Power of the car ", self.hp)
        print("This is a car")


c1 = Car(300, 300000, 6, 9999)
c1.show_details()
