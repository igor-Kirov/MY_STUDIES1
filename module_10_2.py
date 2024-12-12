from time import sleep, time
import  threading


class Knight(threading.Thread):
    def __init__(self,name, power,paus):
        threading.Thread.__init__(self)
        self.name=name
        self.power=power
        self.paus=paus
    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        kol_day = 0
        while enemy:
            enemy-=self.power
            print(f'{self.name} сражается {kol_day} дней(дня)..., осталось {enemy} воинов.')
            kol_day += 1
            sleep(self.paus)
        print(f'{self.name} одержал победу спустя {kol_day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10,1.1)
first_knight.start()
second_knight = Knight("Sir Galahad", 20,1)
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')