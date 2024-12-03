from random import choice

class MysticBall:
    __words = ()
    def __init__(self, *words):
        self.__words = words

    def __call__(self):
        return choice(self.__words)


first = 'Мама мыла раму'
second = 'Рамена мало было'
rez = list(map(lambda x, y: x == y , first, second))
print(rez)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for s in data_set:
           file.write(str(s)+'\n')
        file.close()
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())