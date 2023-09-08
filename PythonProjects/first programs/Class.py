class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')

na = input('Name: ')
person1 = Person(na)
person1.talk()