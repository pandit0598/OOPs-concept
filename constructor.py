class Employee():
    def __init__(self, name, salary, age, gender):
        self.name = name
        self.salary = salary
        self.age = age
        self.gender = gender

    def show_employee_details(self):
        print("Employee name is ", self.name)
        print("Employee salary is ", self.salary)
        print("Employee age is ", self.age)
        print("Employee gender is ", self.gender)


p1 = Employee("Jose", 25000, 25, "Male")

p1.show_employee_details()
