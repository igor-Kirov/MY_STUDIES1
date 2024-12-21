from threading import Thread
import time
import random
import queue



class Table:
    def __init__(self,number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        self.name_ = name
        super().__init__()

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:
    _queue = queue.Queue()
    _guests =[]

    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests ):
        n=0
        for y in guests:
                while n<len(self.tables):
                #for i in range(n, len(self.tables)):
                    if self.tables[n].guest==None:
                        self._guests.append(y)
                        self.tables[n].guest = y.name_
                        self._guests[n].start()
                        print(f'{y.name_} сел(-а) за стол номер {self.tables[n].number}')
                        n+=1
                        break
                    else:
                        n += 1
                else:
                    print(f'{y.name_} в очереди')
                    self._queue.put(y)



    def discuss_guests(self):
        n=0
        while True:
            #print(n)
            if self.tables[n].guest !=None:
                if self._guests[n].is_alive():
                    s = self.tables[n].guest
                    print(f'{s} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables[n].number} свободен')
                    self.tables[n].guest =None
                    if not self._queue.empty():
                        self._guests[n]=self._queue.get(timeout=10)
                        self.tables[n].guest= self._guests[n].name_
                        self._guests[n].start()
                        print(f'{self.tables[n].guest} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[n].number}')
            else:
                exit()

            if n < len(self.tables)-1:
                n += 1
            else:
                n = 0


queue = queue.Queue()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
            'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
            'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
        ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
