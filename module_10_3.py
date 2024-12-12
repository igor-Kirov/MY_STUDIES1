import  threading
import  random
from time import sleep

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
       for i in range(1,100):
        sleep(0.001)
        put_sum = random.randint(50,500)
        self.balance +=put_sum
        print(f'Пополнение: {put_sum}. Баланс: {self.balance} ')
        if self.balance >= 500:
            if lock.locked():
                lock.release()
        else:
            if not lock.locked():
               lock.acquire()

    def take(self):
       lock.acquire()
       for i in range(1, 100):
           sleep(0.001)
           put_sum = random.randint(350, 500)
           print(f'Запрос на {put_sum}. ')
           if self.balance >= put_sum:
               self.balance -= put_sum
               print(f'Снятие: {put_sum}. Баланс: {self.balance} ')
           else:
               print('Запрос отклонён, недостаточно средств ')
               if not lock.locked():
                    lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')