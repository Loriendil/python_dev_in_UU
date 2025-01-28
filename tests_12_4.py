# Код для домашнего задания по теме "Логирование"
import logging
from contextlib import contextmanager
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        format='%(asctime)s : %(levelname)s - %(message)s',
                        encoding="utf-8")
logging.info("Начало тестирования")

# В уроке такая глупость рассказана. Зачем нам писать по 100 раз одно и тоже,
# если можно показать студентам, что можно написать (ну, или напомнить / подсказать) один раз
# обернув функцию в декораторе контекст менеджера!
# У нас, конечно, давали ОЧЕНЬ плохо эту историю, так что впечатление об этом осталось как о заумной фигне и
# действия лектора к такой мысли и способствуют, и поощряют, но ведь это не так!

@contextmanager
def log_exceptions(*exceptions):
    try:
        yield
    except Exception as e:
        if isinstance(e,exceptions):
            logging.warning(f'{type(e).__name__} \n '
                            f'Возникло исключение: {e}. Пояснение: Неверный тип данных для объекта Runner',
                            exc_info=True)
        else:
            logging.critical(f'{type(e).__name__} \n Возникло исключение: {e}. '
                             f'Пояснение: Неверный тип данных для объекта Runner', exc_info=True)
            raise  # Переподнимаем если это не одна из специфических исключений

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Tests in this case are frozen")
    def test_walk(self):
        with log_exceptions(BaseException):
            first_runner = Runner("Alex", -5)
            for i in range(10):
                first_runner.walk()
            self.assertEqual(first_runner.distance, 50)
            logging.info("test_walk выполнен успешно")

    @unittest.skipIf(is_frozen, "Tests in this case are frozen")
    def test_run(self):
        with log_exceptions(BaseException):
            second_runner = Runner(['Vlad'])
            for i in range(10):
                second_runner.run()
            self.assertEqual(second_runner.distance, 100)
            logging.info('test_run" выполнен успешно')


    @unittest.skipIf(is_frozen, "Tests in this case are frozen")
    def test_challenge(self):
        third_runner = Runner("Vika")
        forth_runner = Runner("Olga")

        for i in range(10):
            third_runner.run()
            forth_runner.walk()

        self.assertNotEqual(third_runner.distance, forth_runner.distance)

if __name__ == '__main__':
    unittest.main()
