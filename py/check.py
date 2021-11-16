class Student:
    def __init__(self, ismi, yoshi,):
        self.ismi = ismi
        self.yoshi = yoshi

    def __str__(self):
        return f"{self.ismi}, {self.yoshi} "

    def __eq__(self, other):
        return self.yoshi == other.yoshi

    def __lt__(self, other):
        return self.yoshi < other.yoshi

    def __gt__(self, other):
        return self.yoshi > other.yoshi

jhon = Student("John", 21)
bob = Student("Bob", 32)
alice = Student("Alice", 21)

print(jhon > bob)
print(jhon < bob)
print(jhon == alice)




