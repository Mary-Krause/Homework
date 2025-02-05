import unittest
from for_test import Runner  # Импортируем класс Runner из нужного модуля


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("TestRunner1")  # Создаем объект
        for _ in range(10):
            runner.walk()  # 10 раз вызываем walk
        self.assertEqual(runner.distance, 50)  # Проверяем, что расстояние = 50

    def test_run(self):
        runner = Runner("TestRunner2")  # Создаем объект
        for _ in range(10):
            runner.run()  # 10 раз вызываем run
        self.assertEqual(runner.distance, 100)  # Проверяем, что расстояние = 100

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()  # Первый объект бегает
            runner2.walk()  # Второй объект ходит

        self.assertNotEqual(runner1.distance, runner2.distance)  # Проверяем, что дистанции разные


if __name__ == "__main__":
    unittest.main()



# Инструкции по запуску тестов:
# Убедитесь, что в папке for_test есть файл с классом Runner.
# Запустите тесты командой:
# python -m unittest runner_tests.py
# Должно появиться сообщение:
# Ran 3 tests in 0.001s
# OK

# Попробуйте изменить ожидаемое значение в assertEqual и запустите тесты снова, чтобы увидеть, как тесты ловят ошибки.