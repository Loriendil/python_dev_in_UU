# Домашнее задание по теме "Простые Юнит-Тесты"

import runner as rn
import unittest as un

class RunnerTest(un.TestCase):
    def test_walk(self):
        first_runner = rn.Runner("Alex")
        for i in range(10):
            first_runner.walk()
        self.assertEqual(first_runner.distance, 50)

    def test_run(self):
        second_runner = rn.Runner("Vlad")
        for i in range(10):
            second_runner.run()
        self.assertEqual(second_runner.distance, 100)
        # self.assertLess(second_runner.distance, 10) Меняю значение в тесте, чтобы посмотреть результаты

    def test_challenge(self):
        third_runner = rn.Runner("Vika")
        forth_runner = rn.Runner("Olga")

        for i in range(10):
            third_runner.run()
            forth_runner.walk()

        self.assertNotEqual(third_runner.distance, forth_runner.distance)

if __name__ == '__main__':
    un.main()