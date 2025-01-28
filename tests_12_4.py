# Код для домашнего задания по теме "Логирование"
import logging

from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        format='%(asctime)s : %(levelname)s - %(message)s',
                        encoding="utf-8")
logging.info("Начало тестирования")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Tests in this case are frozen")
    def test_walk(self):
        try:
            first_runner = Runner("Alex", -5)
            for i in range(10):
                first_runner.walk()
            self.assertEqual(first_runner.distance, 50)
            logging.info("test_walk выполнен успешно")
        except TypeError as err1:
            logging.warning(f'Неверный тип данных для объекта Runner: {err1.args}', exc_info=True)
        except ValueError as err2:
            logging.warning(f'Неверный тип данных для объекта Runner: {err2.args}', exc_info=True)
        except Exception as err3:
            logging.critical(f'Неверный тип данных для объекта Runner: {err3.args}', exc_info=True)

    @unittest.skipIf(is_frozen, "Tests in this case are frozen")
    def test_run(self):
        try:
            second_runner = Runner(['Vlad'])
            for i in range(10):
                second_runner.run()
            self.assertEqual(second_runner.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError  as err4:
            logging.warning(f'Неверный тип данных для объекта Runner: {err4.args}',  exc_info=True)
        except ValueError  as err5:
            logging.warning(f'Неверный тип данных для объекта Runner: {err5.args}',  exc_info=True)
        except Exception  as err6:
            logging.critical(f'Неверный тип данных для объекта Runner: {err6.args}', exc_info=True)


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