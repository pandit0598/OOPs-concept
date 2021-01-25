class Employee:
    def __init__(self, name, company, retired='NO'):
        self.__name = name
        self.__company = company
        self.__retired = retired

    @property
    def company(self):
        print("@property class method called: ")
        return self.__company

    @company.setter
    def company(self, value):
        print("@company.setter class method called: ")
        self.__company = value


e = Employee("Prafull", "Amazon")
print("Company name is : ", e.company)
print("=" * 35)
e.company = "Google"
print("Company name is : ", e.company)
print("=" * 35)
Employee.company = "Microsoft"
print("Company name is : ", Employee.company)





