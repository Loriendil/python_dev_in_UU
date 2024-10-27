# Домашняя работа по уроку "Способы вызова функции"
# создаём функцию, которая получает 3 параметра. 2 позиционных (message, receiver) и 1 именованный (sender).
"""" Первая версия программы после просмотра видео """
def send_email(message, recipient, sender = 'university.help@gmail.com'):
# Проверка на корректность e-mail отправителя и получателя.
    address_sign = '@'
    allowed_domain = ['.com', '.ru', '.net']
    is_address_r = False
    is_address_s = False
    if address_sign in recipient:
        for item in allowed_domain:
            if item in recipient:
                is_address_r = True
            if item in sender:
                is_address_s = True

    if not is_address_r or  not is_address_s:
        print(f'1. Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

# Проверка на отправку самому себе.
    elif sender == recipient:
        print(f'2. Нельзя отправить письмо самому себе!')

# Проверка на отправителя по умолчанию.
    elif sender == 'university.help@gmail.com':
        print(f'3. Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'4. НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


"""Вторая версия программы, после того, как я погуглил и разобрал советы ИИ по улучшению программы"""
# Проверка на корректность e-mail отправителя и получателя.
# Вынесем в отдельную функцию, чтобы увеличить читаемость кода
def is_valid_email(email):
    #ИИ сюда пихает проверку на наличие '@' в строке адреса, но это противоречит ТЗ. Забавно.
    address_sign = '@'
    allowed_domain = ['.com', '.ru', '.net']
    # domain = email.split('@')[-1] это сокращённая запись кода:
    # domain = email.split('@')
    # domain = domain[1]
    # выгода написать [-1] выгоднее чем [1] в том, что [-1] показывает, что читаем с конца,
    # а так без разницы. Работает и так, и так.
    # Поскольку вне зависимости от исхода обучения эти упражнения всё равно останутся со мной, то
    # вот ссылка на документацию для памяти:
    # https://docs.python.org/3/library/stdtypes.html#str.split
    domain = email.split(address_sign)[-1]
    # Тут будет "грязная магия".
    # функция endswith() - возвращает True, если строка кончается на указанное value, в противном случае - False
    # Искомое может быть кортежем, что кстати, но не тут. У нас список, который мы можем привычно поменять
    # в любой момент. Ссылка на документацию для памяти:
    # https://docs.python.org/3/library/stdtypes.html#str.endswith
    # Искомое у нас готово в переменной domain, поэтому программное выражение: d = domain.endswith('.com') поместит
    # в переменную d значение 'ИСТИНА' или 'ЛОЖЬ'. По условию задачи нам нужно проверить 3 таких окончания адреса,
    # поэтому нужен цикл. Напрашивается цикл:
    # for item in allowed_domain:
    #    if domain.endswith(item):
    #       print('Есть контакт!')
    # НО! Среди встроенных функций есть функция any()! Судя по тому, что написано о ней в документации
    # она делает буквально то же, что и в коде выше. Однако, эрудиция помогает обширнее пользоваться встроенным
    # стабильным функционалом, но увеличивает зависимости в коде от стандартных библиотек.
    # Пользоваться или нет вопрос вкуса, я вслед за ИИ использую, хотя можно и немного удлинить текст программы
    # наверное. Ссылка на документацию: https://docs.python.org/3/library/functions.html#any
    if  any(domain.endswith(suffix) for suffix in allowed_domain):
    # в документации сказано кстати вот так: str.endswith(suffix[, start[, end]]),
    # а мы пишем вот так: any(domain.endswith(suffix) for suffix in allowed_domain) и
    # почему это работает казалось бы.
    # Цикл под капотом каждый раз формирует для any() список (ну, или любой итерируемый объект, но я тестил на списке)
    # и подсовывает в any(), где первый элемент и единственный элемент это результат вызова функции endswith().
    # это так потому, что если выкинуть цикл, то получится вот такой код:
    # print(domain.endswith('.com'))
    # print(domain.endswith('.ru'))
    # print(domain.endswith('.net'))
    # print(any([domain.endswith('.com')]))
    # print(any([domain.endswith('.net')]))
    # print(any([domain.endswith('.net')]))
    # Это конечно всё мысли гипотетически и хорошо бы почитать про то, как работает интерпретатор на самом деле.
    # Книжки типа Рихтер "CLR via C#. Программирование на платформе Microsoft .NET Framework 4.0 на языке C#" для
    # Python я не нашёл, но я и искал на самом деле, потому что читать такие книжки нужно всё же уже понимая как
    # работать с инструментом, а не до этого. В этом на самом деле и есть не преодолимый недостаток ИИ. Оно может
    # дать тебе код, но почему он работает или нет - должен разобраться сам.
        return True
    else:
        return False

def send_email_upd(message, recipient, sender = 'university.help@gmail.com'):
# в этой функции ИИ не даёт нормального решения, поэтому переписываю я её сам.
# Логические выражения это чёрная магия, но кажется я успешно справился.
    default_email = 'university.help@gmail.com'
    address_sign = '@'
# Проверим самое очевидно - отправку самому себе
    if sender == recipient:
        print(f'2. You can\'t send a letter to yourself!')
        return False

#  В начале проверяем, чтобы строки recipient и sender содержали "@" и оканчивались на ".com"/".ru"/".net"
    if not ((address_sign in sender and address_sign in recipient) and is_valid_email(sender)):
        print(f'1. Unable to send email from {sender} to {recipient}')
        return False

# если допустимый отправитель, отправляем сообщение
    if  is_valid_email(sender) and sender == default_email:
        print(f'3. Email successfully sent from {sender} to {recipient}.')
        return False

# если недопустимый отправитель, уведомляем, о том что отправитель необычный
    elif is_valid_email(sender) and sender != default_email:
        print(f'4. UNUSUAL SENDER! Message sent from {sender} to {recipient}.')

    return True

print('-------------------------вызов send_email()--------------------------------------')
# Примеры вызовов из задания:
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

print('-------------------------вызов send_email_upd()--------------------------------------')

# Мои примеры:
send_email_upd('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email_upd('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email_upd('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email_upd('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
