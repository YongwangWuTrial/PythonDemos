class User(None):
    def __init__(self, name="", age=20, sex="Male"):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "{0:<10}:{1:<10},{2:<10}".format(self.name, self.sex, self.age)

    def __le__(self, other):
        if not other.isinstance(User):
            return None
        return self.age < other.age
