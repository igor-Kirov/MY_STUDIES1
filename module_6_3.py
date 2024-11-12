import random

class Animal:
    live=True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._corde=[0,0,0]
        self.speed=speed
    def move(self,dx,dy,dz):
        if dz * self.speed > 0:
            self._corde[0] = dx * self.speed
            self._corde[1] = dy * self.speed
            self._corde[2]  = dz * self.speed
        else:
            print('It''s too deep, i can''t dive :(')

    def get_cords(self):
        print(f'X:{self._corde[0]}, Y: {self._corde[1]}, Z: {self._corde[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, i''m peaceful :)')
        else:
            print('Be careful, i''m attacking you 0_0')

class Bird(Animal):
    beak = True

    def __init__(self, speed=0):
        super().__init__(speed)

    def lay_eggs(self):
       print(f'Here are(is) {random.randint(1, 4)}  eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self,dz):
        fei = int(self._corde[2]  - abs(dz)/ 2 * self.speed)
        self._corde[2] = fei

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'
    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()  # метод в задании отсутствует
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()