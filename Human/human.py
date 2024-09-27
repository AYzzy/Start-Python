class Human:
    number_of_eye = 2

    def __init__(self, name, nin=None, age=12):
        self.name = name
        self.age = age

    def get_nack(self):
        print("Nacking...")

    def get_details(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        """


h1 = Human("samuel", age=32)
h2 = Human("chidinma", age=22)
h3 = Human("jonah", age=33)

Human.number_of_eye = 4

print(h2.get_details())

print(h1.age)
