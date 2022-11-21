class Mammals:
    def walk(self):
        print('*walking')
class Feline(Mammals):
    def roar(self):
        print('ROAR!!')
class Cat(Feline):
    def meow(self):
        print('meow')


cat = Cat()
cat.walk()