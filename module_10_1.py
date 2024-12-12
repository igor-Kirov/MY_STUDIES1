from time import sleep, time
import  threading
import datetime

def stime(func):
    def wrapper(*args):
        start_time_fun = time()
        func(*args)
        end_time_fun = time()
        diff_time = end_time_fun - start_time_fun
        print('Работа потока: ', datetime.timedelta(seconds=diff_time))
    return wrapper

def write_words(sword_count=1,file_name=''):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, sword_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print('Работа потоков: ', datetime.timedelta(seconds=time() - start_time))


thread5 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thread6 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread7 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread8 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

start_time = time()

thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

print('Работа потоков: ', datetime.timedelta(seconds=time() - start_time))
