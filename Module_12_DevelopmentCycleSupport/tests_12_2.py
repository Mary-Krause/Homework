import unittest
from for_test_2 import Runner, Tournament  # Импортируем классы Runner и Tournament из нужного модуля

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Создаем атрибут класса для хранения результатов тестов

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        self.__class__.all_results[1] = tournament.start()
        self.assertTrue(max(self.__class__.all_results[1].keys()) == 2 and self.__class__.all_results[1][2] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        self.__class__.all_results[2] = tournament.start()
        self.assertTrue(max(self.__class__.all_results[2].keys()) == 2 and self.__class__.all_results[2][2] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        self.__class__.all_results[3] = tournament.start()
        self.assertTrue(max(self.__class__.all_results[3].keys()) == 3 and self.__class__.all_results[3][3] == "Ник")

if __name__ == "__main__":
    unittest.main()
