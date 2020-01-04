class Person:
    def __init__(self,name):
        self.name = name
        
    def talk(self):
        print(f'Hi, my name is {self.name}')


Andre = Person("Andre")
Andre.talk()