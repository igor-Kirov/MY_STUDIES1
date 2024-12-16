from time import sleep, time
import  threading, multiprocessing
import datetime

def read_info(name):
    all_data=[]
    with open(name, encoding='utf-8') as file:
        for i in file:
            if file.readline() != '':
                all_data.append(file.readline())
            else:
                break
filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    start = time()
    for i in filenames:
        # print(i)
        read_info(i)
    end = time()
    diff = end - start
    print(datetime.timedelta(seconds=diff), '(линейный)')

    start_time_fun = time()
    with multiprocessing.Pool(len(filenames)) as p:
        p.map(read_info, filenames)
    end_time_fun = time()
    diff_time = end_time_fun - start_time_fun
    print(datetime.timedelta(seconds=diff_time), '(многопроцессный)')