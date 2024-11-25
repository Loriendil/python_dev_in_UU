# Дополнительное практическое задание по модулю: "Классы и объекты."
from time import sleep

class User:
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname:str, password:str):
        """Вход: имя пользователя nickname и пароль пользователя password.
        Действие: log_in() метод ищет пользователя с пара значений: имя пользователя nickname и
        пароль пользователя password. Пароль хэшируется и сравнивается с хеш-суммой хранимой в базе данных.
        Выход: выставляет регистрируемого пользователя в качестве текущего или сообщает об отсутствии такового"""

        # Официальная документация (ссылки:
        # https://docs.python.org/3/library/hashlib.html#simple-hashing
        # https://docs.python.org/3/library/hashlib.html#key-derivation)
        # в отличие от ссылок в задании говорит о том как нужно конкретно использовать хранение паролей, но
        # в задаче у нас явно сказано сделать это с помощью магической функции __hash__(), поэтому переопределим
        # метод __eq__() для __hash__()

        for user in self.users:
            if user.nickname == nickname and user.password == user.__hash__(password):
                self.current_user = user
                return
        print('Incorrect pair of login and password. Check input.')

    def register(self, nickname: str, password: str, age: int):
        """Вход: имя пользователя nickname, пароль password, возраст age
           Действие: Метод register() проверяет наличие пользователя и вносит нового уникального пользователя
           Выход: создание нового пользователя, переключение текущего пользователя на нового уникального пользователя
           или сообщает о наличие такого пользователя"""

        #Применим военную хитрость как говорится. Прямолинейный вариант это сделать условный переход.
        # Однако, если мы в конце проверки условия используем return, то блок условия завершится выходом из метода.
        # Меньше переменных, меньше ветвлений, короче код, больше лаконичность. Красота!
        for user_name in self.users:
            if nickname is user_name.nickname:
                print(f'Пользователь {nickname} уже существует!')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return

    def log_out(self):
        """Вход: ничего
           Действие: закрытие сессии путём сброса значения текущего пользователя в None.
           Выход: ничего"""
        self.current_user = None

    def add(self, *vids: Video):
        """Вход: картеж экземпляров типа Video
           Действие: добавление новых уникальных видео в список уже имеющихся видео
           Выход: ничего"""
        for vid in vids:
            if vid not in self.videos:
                self.videos.append(vid)

    def get_videos(self, search_word: str):
        """
        Вход: поисковое слово
        Действие: поиск по поисковому слову без учёта регистра в названиях роликов поискового слова
         Выход: список всех найденных фильмов
        """
        found_videos = []
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                found_videos.append(video)

        for found_video in found_videos:
            result.append(found_video.title)

        return result

    def watch_video(self, movie_title:str):
        # Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        # В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        # Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
        # так как есть ограничения 18+ и выводиться соответствующее сообщение.
        if self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        # Если условие в цикле не выполниться, значит названия фильма нет и, следовательно, ничего не воспроизведётся.
        # Если условие выполнено, то запуститься цикл отображающий отсчёт времени, на которой ведётся просмотр.
        # По выходу из цикла переменная index исчезает и соответственно её значение утрачивается.
        # Окончание просмотра проявляется в виде сообщения в консоли.
        for video in self.videos:
            if movie_title is video.title:
                for index in range(1, 11, 1):
                    sleep(0.2)
                    print(index)
                print('Конец видео')

if __name__ == '__main__':
    #Код для проверки:
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