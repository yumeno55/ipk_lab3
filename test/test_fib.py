import main.my_lib
import pytest

# Тест функции, определющей n чисел Фибоначчи
class TestFib():
    # Тестируем программу на корректных данных. Функция возвращает список элементов
    def test_on_correct_n(self):
        assert main.my_lib.fib(6) == [1, 1, 2, 3, 5, 8]

    # Тестируем программу на некорректных данных. Функция вызывает исключение TypeError
    def test_on_str_n(self):
        with pytest.raises(TypeError):
            main.my_lib.fib('1')

    # Тестируем программу при n < 1. Функция возвращает пустой список список
    def test_on_negative_n(self):
        assert main.my_lib.fib(-2) == []