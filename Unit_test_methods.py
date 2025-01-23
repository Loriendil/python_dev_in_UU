# Домашнее задание по теме "Методы Юнит-тестирования"
import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Test: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def setUp(self):
        self.Usain_runner = Runner("Usain", 10)
        self.Andrey_runner = Runner("Andrey", 9)
        self.Nick_runner = Runner("Nick", 3)


    def test_us_vs_uk(self):
        unreal_tournament_us_vs_uk = Tournament(90,
                                                self.Usain_runner, self.Nick_runner)
        result = unreal_tournament_us_vs_uk.start()
        self.assertTrue(result[list(result.keys())[-1]] == "Nick", "Nick should be a last runner!")
        self.all_results['test_round_us_vs_uk'] = result

    def test_uk_vs_rus(self):
        unreal_tournament_uk_vs_ru = Tournament(90,
                                                self.Andrey_runner, self.Nick_runner)
        result = unreal_tournament_uk_vs_ru.start()
        self.assertTrue(result[list(result.keys())[-1]] == "Nick", "Nick should be a last runner!")
        self.all_results['test_round_rus_vs_uk'] = result

    def test_international(self):
        international_unreal_tournament =  (
                            Tournament(90,
                                       self.Usain_runner, self.Andrey_runner, self.Nick_runner))
        result = international_unreal_tournament.start()
        # max_value = max(self.all_results, key=self.all_results.get) для этого нужно перегрузить __lt__, __gt__
        # но исходные классы в задании не позволяют так делать!
        self.assertTrue(result[list(result.keys())[-1]] == "Nick", "Nick should be a last runner!")
        self.all_results['test_olympic_round'] = result

    def test_refactoring_provided_code(self):
        # 1. Удаление объекта из списка participants может до завершения цикла до запуска метода participant.run()
        # вместо for participant in self.participants:
        # нужно написать for participant in self.participants[:]:
        # 2. Так же тут нужен булевый флаг для выхода из бесконечного цикла, так что тут на самом деле не одна ошибка, а
        # их две, не говоря уже о том, что сам класс Runner до ума не доведён.

        refactoring_unreal_tournament = (
            Tournament(8,
                       self.Usain_runner, self.Andrey_runner, self.Nick_runner))
        result = refactoring_unreal_tournament.start()
        self.assertTrue(result[list(result.keys())[-1]] == "Nick", "Nick should be a last runner!")
        self.all_results['test_bonus_round'] = result

if __name__ == "__main__":
    unittest.main()