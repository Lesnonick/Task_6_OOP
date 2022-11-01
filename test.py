class Person:
    def __init__(self, id):
        self.id = id

some_person = Person(100)
some_person.__dict__['age'] = 30
print(some_person.age + len(some_person.__dict__))

class Income:
    def __init__(self, id_):
        self.id_ = id_
        id_=100
income_1 = Income(1000)
print(income_1.id_)

print(isinstance(some_person, Person))
