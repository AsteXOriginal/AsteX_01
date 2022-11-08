class Animal():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        print(f'The animal with name {self.name} created')

    def eat(self):
        print(f'The animal {self.name} is eating')
    def go(self, miles):
        print(f'The animal {self.name} go for{miles}, miles')
animal = Animal('Lora', 5, 'labrador')

animal.eat()

animal.go(10)
input()
