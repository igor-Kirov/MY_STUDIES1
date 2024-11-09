class Animal:
    name = ''
    alive = True
    fed = False
    def __init__(self,name, alive=True, fed=False):
        self.name= name
        self.alive = alive  #живой
        self.fed = fed   #накормленный
    pass

class Plant:
    name = ''
    edible = False
    def __init__(self,name, edible=False):
        self.name = name
        self.edible = edible #съедобность
    pass

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                self.alive = False
    pass

class Predator (Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                self.alive = False
        pass
class Flower(Plant):
     pass

class Fruit(Plant):
    def __init__(self, name, edible=True):
        self.name = name
        self.edible = True  # съедобность
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)