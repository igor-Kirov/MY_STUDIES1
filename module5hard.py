#
import time


class User:
    def __init__(self, nickname='', password=0, age=0):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # в хэшированном виде, число
        self.age = age  # возраст, число

    def __str__(self):
        name = self.nickname
        return name

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = 0  # секунда остановки
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)


class UrTube:
    def __init__(self) -> object:
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, User


    def log_in(self, nickname, password):
        for u in self.users:
            if nickname == u.nickname and hash(password) == u.password:
                self.current_user = u
            else:
                self.current_user = None
        pass

    def register(self, nickname, password, age):
        rif = True
        user1 = User(nickname, hash(password), age)
        for u in self.users:
            if nickname == u.nickname:
                print(f'Пользователь {nickname} уже существует')
                if hash(password) == u.password:
                    self.current_user = u
                rif = False
        if rif:
            self.users.append(user1)
            self.current_user = user1
        pass

    def log_out(self):  # для сброса текущего пользователя на None.
        self.current_user = None
        pass

    def add(self, *args):  # объектов класса Video и все добавляет в videos,
        for i in args:
            self.videos.append(i)
        pass

    def get_videos(self, word):  # поисковое слово и возвращает список названий всех видео
        list_title = []
        for n in self.videos:
            if word.upper() in n.title.upper():
                list_title.append(n.title)
        return list_title
        pass

    def watch_video(self, title):  # находит - ведётся отчёт в консоль на какой секунде ведётся просмотр
        if self.current_user is not None:
            for n in self.videos:
                if title == n.title:
                    if self.current_user.age > 17 and n.adult_mode:
                        for y in range(1, n.duration+1):
                            time.sleep(1)
                            print(y,' ', end='')
                        print("Конец видео")
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
        pass


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

