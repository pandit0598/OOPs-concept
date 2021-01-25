class Parent1:
    def assign_string_one(self, str1):
        self.str1 = str1
    def show_string_one(self):
        return self.str1


class Parent2:
    def assign_string_two(self, str2):
        self.str2 = str2
    def show_string_two(self):
        return self.str2


class Child(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3


mychild = Child()
mychild.assign_string_one("I am Parent1")
mychild.assign_string_two("I am Parent2")
mychild.assign_string_three("I am Child")
mychild.show_string_one()
mychild.show_string_two()
mychild.show_string_three()
